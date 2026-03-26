# sync-to-github.ps1
# Run this script from the vla-expert-skill repo directory to push daily updates
# Usage: .\scripts\sync-to-github.ps1

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$sourceMemory = "$env:USERPROFILE\KW_VLA\scripts\vla-expert\VLA_EXPERT_MEMORY.md"
$targetMemory = "$repoRoot\skill\references\VLA_EXPERT_MEMORY.md"

Write-Host "🔄 VLA Expert Skill — Sync to GitHub" -ForegroundColor Cyan
Write-Host ""

# Check source file exists
if (-not (Test-Path $sourceMemory)) {
    Write-Host "❌ Source file not found: $sourceMemory" -ForegroundColor Red
    exit 1
}

# Copy updated memory file
Write-Host "📋 Copying updated VLA_EXPERT_MEMORY.md..."
Copy-Item $sourceMemory $targetMemory -Force

# Check for changes
Set-Location $repoRoot
$status = git status --porcelain
if (-not $status) {
    Write-Host "✅ No changes detected. Knowledge base is already up to date." -ForegroundColor Green
    exit 0
}

# Commit and push
$today = Get-Date -Format "yyyy-MM-dd"
$header = (Get-Content $targetMemory -TotalCount 1) -replace "# ", ""

Write-Host "📦 Changes detected, committing..."
git add skill/references/VLA_EXPERT_MEMORY.md
git commit -m "📚 Daily knowledge base update — $today`n`n$header"
git push origin main

Write-Host ""
Write-Host "✅ Successfully synced to GitHub!" -ForegroundColor Green
Write-Host "   Updated: $today"
Write-Host "   Version: $header"
