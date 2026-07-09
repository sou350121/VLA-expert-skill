#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-expert-memory.py — Self-sustaining daily regenerator for the
VLA-expert-skill knowledge base (skill/references/VLA_EXPERT_MEMORY.md).

Revives the server-side `vla-expert-bot` pipeline that died 2026-06-26.

DESIGN (conservative, no-degradation):
  * MECHANICAL / deterministic (no LLM):
      - patch version bump + date -> TODAY (TODAY is supplied by the cron
        wrapper; this script never invents "now" for the KB date so runs are
        reproducible).
      - refresh the `> **来源**` count line from ACTUAL handbook file counts.
      - APPEND (never delete) to §11 论文速查 any NEW paper-dissections added to
        the handbook since the KB's own header date (derived from git log on
        theory/). Dedup against arxiv ids already present.
      - RECOMPUTE the Source Map 行号 column from the final section offsets.
  * LLM (qwen / DashScope), ONE guarded call only:
      - produce ONE dated `> **vX.Y 变更摘要**（TODAY 自动重生）：…` line to
        PREPEND to the changelog stack, grounded in the new deep-dives + current
        mainlines. If the call fails, fall back to a deterministic mechanical
        summary line (the pipeline must stay self-sustaining offline).
      - the LLM is NEVER asked to rewrite belief confidences (§4), phase %
        (§5), or any §0-§15 body. Those are CARRIED FORWARD VERBATIM.
  * GUARDS before writing (fail loudly, write nothing on failure):
      - all 16 section headers §0-§15 present in the output
      - output length >= 90% of input length
      - new version strictly greater than input version
      - Source Map still has its 16 rows

Usage:  build-expert-memory.py <YYYY-MM-DD>      (TODAY as arg)
   or:  TODAY=<YYYY-MM-DD> build-expert-memory.py
"""

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO = Path("/home/claudeuser/VLA-expert-skill")
KB = REPO / "skill" / "references" / "VLA_EXPERT_MEMORY.md"
CHANGELOG = REPO / "CHANGELOG.md"
HANDBOOK = Path("/home/claudeuser/vla-handbook-work")
THEORY = HANDBOOK / "theory"
ENV_FILE = Path("/home/claudeuser/vla-industry-radar/.env")

MAX_NEW_PAPERS = 80  # safety cap if lastKBdate is very old


def log(msg):
    sys.stderr.write("[build-expert-memory] " + msg + "\n")


def die(msg):
    log("FATAL: " + msg)
    sys.exit(1)


# ---------------------------------------------------------------------------
# .env loader (for DASHSCOPE_API_KEY etc.)
# ---------------------------------------------------------------------------
def load_env(path):
    env = {}
    if not path.exists():
        return env
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        v = v.strip().strip('"').strip("'")
        env[k.strip()] = v
    return env


# ---------------------------------------------------------------------------
# Handbook counts + new-paper discovery
# ---------------------------------------------------------------------------
def count_files(root, suffix):
    n = 0
    for _dirpath, _dirnames, filenames in os.walk(str(root)):
        if os.sep + ".git" in _dirpath:
            continue
        for fn in filenames:
            if fn.endswith(suffix):
                n += 1
    return n


def build_dissection_index():
    """basename -> relpath (relative to HANDBOOK) for every *_dissection.md."""
    idx = {}
    for dirpath, _dirnames, filenames in os.walk(str(THEORY)):
        for fn in filenames:
            if fn.endswith("_dissection.md"):
                full = Path(dirpath) / fn
                idx[fn] = str(full.relative_to(HANDBOOK))
    return idx


def git_added_dissections(since_date):
    """Basenames of *_dissection.md ADDED to theory/ since since_date (newest first, deduped)."""
    try:
        out = subprocess.check_output(
            [
                "git", "-C", str(HANDBOOK), "log",
                "--since=" + since_date + " 00:00",
                "--diff-filter=A", "--name-only", "--pretty=format:",
                "--", "theory/",
            ],
            universal_newlines=True,
            stderr=subprocess.STDOUT,
        )
    except (subprocess.CalledProcessError, OSError) as exc:
        log("WARN: git log for new papers failed: %s" % exc)
        return []
    seen = set()
    result = []
    for line in out.splitlines():
        line = line.strip()
        if not line.endswith("_dissection.md"):
            continue
        base = os.path.basename(line)
        if base in seen:
            continue
        seen.add(base)
        result.append(base)
    return result


def extract_paper_meta(relpath):
    """Pull (title, arxiv_id, positioning) from a dissection file. Best-effort."""
    text = (HANDBOOK / relpath).read_text(encoding="utf-8")
    title = None
    m = re.search(r"\*\*论文\*\*\s*[:：]\s*(.+)", text)
    if m:
        title = m.group(1).strip()
    if not title:
        m = re.search(r"^#\s+(.+)", text, re.MULTILINE)
        if m:
            title = m.group(1).strip()
    if not title:
        title = os.path.basename(relpath).replace("_dissection.md", "")

    arxiv = ""
    m = re.search(r"arxiv\.org/abs/([0-9]+\.[0-9]+)", text)
    if m:
        arxiv = m.group(1)

    positioning = ""
    m = re.search(r"\*\*核心定位\*\*\s*[:：]\s*(.+)", text)
    if m:
        positioning = m.group(1).strip()
    return title, arxiv, positioning


def truncate(s, n):
    s = s.replace("|", "／").replace("\n", " ").strip()
    if len(s) > n:
        return s[: n - 1].rstrip() + "…"
    return s


# ---------------------------------------------------------------------------
# LLM (one guarded call)
# ---------------------------------------------------------------------------
def qwen_one_line(env, old_date, today, new_version, papers, mainline_ctx):
    """Return a single-line change summary (no leading marker) or None on failure."""
    key = env.get("DASHSCOPE_API_KEY")
    if not key:
        log("WARN: DASHSCOPE_API_KEY missing; using mechanical fallback")
        return None
    base = env.get("DASHSCOPE_COMPAT_BASE",
                   "https://dashscope.aliyuncs.com/compatible-mode/v1")
    model = env.get("DASHSCOPE_MODEL", "qwen-plus")

    paper_lines = []
    for (title, arxiv, positioning) in papers[:25]:
        tag = (" (%s)" % arxiv) if arxiv else ""
        paper_lines.append("- %s%s：%s" % (title, tag, truncate(positioning, 120)))
    papers_block = "\n".join(paper_lines) if paper_lines else "（自上次更新以来无新增论文拆解）"

    system = (
        "你是 VLA（Vision-Language-Action）领域的资深分析助手。"
        "只依据用户提供的材料写作，严禁编造论文、数字、置信度或相变百分比。"
        "输出必须是简体中文的单一段落（不换行、不加项目符号、不加标题）。"
    )
    user = (
        "以下是 VLA-Handbook 自 %s 到 %s 之间新增的论文拆解，以及当前各主线摘要。\n\n"
        "【新增论文拆解】\n%s\n\n"
        "【当前主线上下文（节选）】\n%s\n\n"
        "请用 2-4 句话写一条“变更摘要”，概括自 %s 以来 handbook 里真正新增/值得注意的方向，"
        "必须完全基于上述材料，不要提出任何信念置信度或相变百分比的调整（那些由更深的周度流程负责）。"
        "只输出这段文字本身。"
        % (old_date, today, papers_block, mainline_ctx[:5000], old_date)
    )

    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.3,
        "max_tokens": 600,
    }).encode("utf-8")

    url = base.rstrip("/") + "/chat/completions"
    retryable = (429, 500, 502, 503, 504)
    for attempt in range(3):
        try:
            req = urllib.request.Request(
                url, data=body,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + key,
                },
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=90) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            text = payload["choices"][0]["message"]["content"].strip()
            # collapse to a single line
            text = re.sub(r"\s+", " ", text.replace("\n", " ")).strip()
            if text:
                return text
            log("WARN: LLM returned empty content")
            return None
        except urllib.error.HTTPError as exc:
            code = exc.code
            log("WARN: LLM HTTP %s (attempt %d)" % (code, attempt + 1))
            if code not in retryable:
                return None
        except (urllib.error.URLError, OSError, ValueError, KeyError) as exc:
            log("WARN: LLM call failed (attempt %d): %s" % (attempt + 1, exc))
    return None


def gather_mainline_context():
    parts = []
    tracker = THEORY / "benchmark_tracker.md"
    files = sorted(THEORY.glob("*/*_mainline.md"))
    if tracker.exists():
        files = [tracker] + files
    for f in files:
        try:
            head = "\n".join(f.read_text(encoding="utf-8").splitlines()[:12])
        except OSError:
            continue
        parts.append("### %s\n%s" % (f.name, head))
    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# KB parsing helpers
# ---------------------------------------------------------------------------
SECTION_RE = re.compile(r"^##\s+(\d+)\.")
SM_ROW_RE = re.compile(r"^\|\s*§")


def find_section_indices(lines):
    """Return ordered list of (num, line_index) for the 16 numbered ## headers."""
    out = []
    for i, ln in enumerate(lines):
        m = SECTION_RE.match(ln)
        if m:
            out.append((int(m.group(1)), i))
    return out


def find_footer_start(lines):
    for i, ln in enumerate(lines):
        if ln.startswith("*生成自"):
            return i
    return len(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    today = None
    if len(sys.argv) > 1 and sys.argv[1].strip():
        today = sys.argv[1].strip()
    elif os.environ.get("TODAY"):
        today = os.environ["TODAY"].strip()
    if not today:
        die("TODAY not supplied (arg or env). Refusing to guess the date.")
    try:
        datetime.strptime(today, "%Y-%m-%d")
    except ValueError:
        die("TODAY must be YYYY-MM-DD, got: %r" % today)

    if not KB.exists():
        die("KB not found: %s" % KB)
    original = KB.read_text(encoding="utf-8")
    orig_len = len(original)
    lines = original.split("\n")

    # --- parse header: version + date ---
    hm = re.match(r"#\s*VLA\s*专家记忆\s*v(\d+)\.(\d+)\.(\d+)\s*\|\s*(\d{4}-\d{2}-\d{2})",
                  lines[0])
    if not hm:
        die("could not parse KB header line: %r" % lines[0])
    maj, minr, patch = int(hm.group(1)), int(hm.group(2)), int(hm.group(3))
    old_date = hm.group(4)
    old_version = "%d.%d.%d" % (maj, minr, patch)
    new_version = "%d.%d.%d" % (maj, minr, patch + 1)
    log("version %s -> %s ; date %s -> %s" % (old_version, new_version, old_date, today))

    # --- locate structural anchors ---
    sec = find_section_indices(lines)
    if len(sec) != 16 or [n for n, _ in sec] != list(range(16)):
        die("expected 16 numbered sections §0-§15, found %s" % [n for n, _ in sec])
    sec_start = {n: i for n, i in sec}

    # (1) header line
    lines[0] = "# VLA 专家记忆 v%s | %s" % (new_version, today)

    # (2) 来源 count line (mechanical, from real counts)
    theory_md = count_files(THEORY, ".md")
    dissections = count_files(THEORY, "_dissection.md")
    src_idx = None
    for i, ln in enumerate(lines):
        if ln.startswith("> **来源**"):
            src_idx = i
            break
    if src_idx is None:
        die("could not find `> **来源**` line")
    lines[src_idx] = (
        "> **来源**：KW_VLA Handbook（theory %d 篇 Markdown / %d 篇论文拆解，产业分析，周报系统）。"
        % (theory_md, dissections)
    )
    log("来源 counts: %d theory md / %d dissections" % (theory_md, dissections))

    # (3) discover NEW papers since last KB date, dedup against §11
    s11 = sec_start[11]
    s12 = sec_start[12]
    s11_text = "\n".join(lines[s11:s12])
    diss_index = build_dissection_index()
    added = git_added_dissections(old_date)
    new_papers = []
    for base in added:
        relpath = diss_index.get(base)
        if not relpath:
            continue  # added then deleted/relocated-away -> gone
        title, arxiv, positioning = extract_paper_meta(relpath)
        if arxiv and arxiv in s11_text:
            continue  # already present
        if arxiv == "" and title in s11_text:
            continue
        new_papers.append((title, arxiv, positioning, relpath))
        if len(new_papers) >= MAX_NEW_PAPERS:
            break
    log("new papers to append: %d" % len(new_papers))

    # (3b) append rows to §11 (after the last table row of that section)
    if new_papers:
        last_row = None
        for i in range(s11, s12):
            if lines[i].startswith("|"):
                last_row = i
        if last_row is None:
            die("could not find §11 table rows to append after")
        rows = ["| **🆕 自动重生新增（%s）** | | |" % today]
        for (title, arxiv, positioning, relpath) in new_papers:
            tag = (" (%s)" % arxiv) if arxiv else ""
            impact = "见 %s" % relpath
            rows.append("| %s%s | %s | %s |" % (
                truncate(title, 90), tag, truncate(positioning, 110), impact))
        lines[last_row + 1:last_row + 1] = rows

    # (4) LLM change-summary line -> prepend to changelog stack
    env = load_env(ENV_FILE)
    llm_papers = [(t, a, p) for (t, a, p, _r) in new_papers]
    mainline_ctx = gather_mainline_context()
    summary = qwen_one_line(env, old_date, today, new_version, llm_papers, mainline_ctx)
    used_llm = summary is not None
    if not used_llm:
        titles = "、".join(truncate(t, 40) for (t, _a, _p, _r) in new_papers[:6]) or "无"
        summary = (
            "机械增量——自 %s 起 handbook 新增 %d 篇论文拆解（%s%s）；§11 已追加，"
            "来源计数与 Source Map 行号已按最终版面重算；信念网络（§4）与相变状态（§5）"
            "按 CLAUDE.md 纪律原样结转，本次无 LLM 改写、无捏造每日增量。"
            % (old_date, len(new_papers), titles,
               "…" if len(new_papers) > 6 else "")
        )
    stack_line = "> **v%s 变更摘要**（%s 自动重生）：%s" % (new_version, today, summary)

    # find first changelog stack line (after the 维护 metadata line)
    stack_idx = None
    for i, ln in enumerate(lines):
        if re.match(r"^> \*\*v\d", ln):
            stack_idx = i
            break
    if stack_idx is None:
        # fall back to inserting right after the 维护 line
        for i, ln in enumerate(lines):
            if ln.startswith("> **维护**"):
                stack_idx = i + 1
                break
    if stack_idx is None:
        die("could not find changelog stack / 维护 anchor to prepend summary")
    lines[stack_idx:stack_idx] = [stack_line]
    log("changelog summary source: %s" % ("qwen-LLM" if used_llm else "mechanical-fallback"))

    # (5) RECOMPUTE Source Map 行号 from FINAL section offsets ------------------
    sec_final = find_section_indices(lines)
    if len(sec_final) != 16:
        die("post-edit section count != 16 (%d)" % len(sec_final))
    starts = [i for _n, i in sec_final]  # ordered §0..§15
    footer_start = find_footer_start(lines)
    ranges = []
    for k in range(16):
        s = starts[k] + 1  # 1-based line number of the ## header
        if k < 15:
            e = starts[k + 1]  # 1-based line just before next header (=starts[k+1]-1+1)
        else:
            e = footer_start  # 1-based line just before footer block
        ranges.append((s, e))

    sm_rows = [i for i, ln in enumerate(lines) if SM_ROW_RE.match(ln)]
    if len(sm_rows) != 16:
        die("Source Map does not have 16 rows (found %d) before rewrite" % len(sm_rows))
    for k, ri in enumerate(sm_rows):
        cols = lines[ri].split("|")
        # cols[0]='' , cols[1]=' §x name ', cols[2]=' 行号 ', cols[3]=priority, cols[4]=deep-file, cols[5]=''
        if len(cols) < 4:
            die("unexpected Source Map row shape: %r" % lines[ri])
        cols[2] = " %d-%d " % ranges[k]
        lines[ri] = "|".join(cols)

    new_text = "\n".join(lines)

    # (6) GUARDS -----------------------------------------------------------------
    for n in range(16):
        if not re.search(r"(?m)^##\s+%d\." % n, new_text):
            die("guard failed: §%d header missing from output" % n)
    if len(new_text) < 0.90 * orig_len:
        die("guard failed: output length %d < 90%% of input %d" % (len(new_text), orig_len))
    # version strictly greater
    if (maj, minr, patch + 1) <= (maj, minr, patch):
        die("guard failed: version not strictly greater")
    nm = re.match(r"#\s*VLA\s*专家记忆\s*v(\d+)\.(\d+)\.(\d+)", new_text.split("\n", 1)[0])
    if not nm or (int(nm.group(1)), int(nm.group(2)), int(nm.group(3))) <= (maj, minr, patch):
        die("guard failed: output header version not > input")
    final_sm = len(re.findall(r"(?m)^\|\s*§", new_text))
    if final_sm != 16:
        die("guard failed: Source Map has %d rows (expected 16)" % final_sm)
    if find_footer_start(new_text.split("\n")) >= len(new_text.split("\n")):
        die("guard failed: footer block (*生成自) missing")

    # (7) WRITE ------------------------------------------------------------------
    KB.write_text(new_text, encoding="utf-8")
    log("wrote KB: %d -> %d chars" % (orig_len, len(new_text)))

    # prepend CHANGELOG entry
    cl = CHANGELOG.read_text(encoding="utf-8") if CHANGELOG.exists() else "# Changelog\n"
    entry = (
        "## %s — Daily Update\n\n"
        "- KB regenerated v%s -> v%s (auto-regen)\n"
        "- §11 论文速查: appended %d new paper-dissection(s) from VLA-Handbook (since %s); append-only\n"
        "- 来源 counts refreshed: theory %d md / %d dissections\n"
        "- Source Map 行号 recomputed from final section offsets\n"
        "- Belief network (§4) + phase-transition state (§5) carried forward verbatim (no LLM rewrite)\n"
        "- Change-summary line: %s\n\n"
        % (today, old_version, new_version, len(new_papers), old_date,
           theory_md, dissections,
           "qwen-generated" if used_llm else "mechanical fallback (LLM unavailable)")
    )
    if cl.startswith("# Changelog"):
        head, _, rest = cl.partition("\n")
        new_cl = head + "\n\n" + entry + rest.lstrip("\n")
    else:
        new_cl = entry + cl
    CHANGELOG.write_text(new_cl, encoding="utf-8")
    log("prepended CHANGELOG entry for %s" % today)

    log("DONE (LLM=%s, new_papers=%d)" % ("yes" if used_llm else "no", len(new_papers)))


if __name__ == "__main__":
    main()
