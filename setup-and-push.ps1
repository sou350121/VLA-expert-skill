# setup-and-push.ps1
# One-time setup: initialize git repo and push all files to GitHub
# Run from: C:\Users\sou35\KW_VLA\vla-expert-skill\
# Usage: Right-click -> Run with PowerShell, or open PowerShell and run:
#   cd C:\Users\sou35\KW_VLA\vla-expert-skill
#   .\setup-and-push.ps1

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  VLA Expert Skill - GitHub Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Initialize git repo
Write-Host "[1/5] Initializing git repository..." -ForegroundColor Yellow
git init

# Set branch to main
Write-Host "[2/5] Setting branch to main..." -ForegroundColor Yellow
git branch -M main

# Add all files
Write-Host "[3/5] Adding all files..." -ForegroundColor Yellow
git add .

# Commit
Write-Host "[4/5] Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial release: VLA Expert Skill v2

- Compressed knowledge base v1.4 (328+ papers, 15 sections)
- Adversarial Triad Debate protocol (Bull/Bear/Arbiter)
- 8 response modes with intent routing
- Calibration discipline + anti-hallucination protocol
- GitHub Actions daily update workflow"

# Add remote and push
Write-Host "[5/5] Pushing to GitHub..." -ForegroundColor Yellow
git remote add origin https://github.com/sou350121/vla-expert-skill.git
git push -u origin main

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  Done! Your repo is live at:" -ForegroundColor Green
Write-Host "  https://github.com/sou350121/vla-expert-skill" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Green
