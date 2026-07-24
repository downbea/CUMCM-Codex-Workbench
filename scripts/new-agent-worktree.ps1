[CmdletBinding()]
param([Parameter(Mandatory=$true)][string]$TaskName)
$ErrorActionPreference='Stop'
$slug=($TaskName -replace '[^A-Za-z0-9_-]','-').ToLower()
$branch="agent/$slug"
$path=Join-Path $PSScriptRoot "..\worktrees\$slug"
if (Test-Path $path) { throw "Worktree already exists: $path" }
git worktree add -b $branch $path HEAD
Write-Host "Created $path on $branch"
