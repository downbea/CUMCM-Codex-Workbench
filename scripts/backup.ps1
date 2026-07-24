[CmdletBinding()]
param([string]$Message = "chore: automatic checkpoint")
$ErrorActionPreference = 'Stop'
$dirty = git status --porcelain
if (-not $dirty) { Write-Host 'No changes to back up.'; exit 0 }
git add .
git commit -m $Message
git push
