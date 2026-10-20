# Local draft preparation only; publication requires maintainer review.
param([Parameter(Mandatory=$true)][string]$Handbook)
$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
python "$repoRoot/scripts/build-expert-memory.py" --handbook $Handbook
if ($LASTEXITCODE -ne 0) { throw "VLA Expert draft generation failed" }
python "$repoRoot/scripts/build-expert-memory.py" --handbook $Handbook --check
if ($LASTEXITCODE -ne 0) { throw "VLA Expert draft validation failed" }
Write-Host "Draft validated. Review the diff before any commit or push."
