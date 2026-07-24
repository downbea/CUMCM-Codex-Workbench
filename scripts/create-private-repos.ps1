[CmdletBinding()]
param([string]$Root = "D:\obsidian笔记")
$ErrorActionPreference = 'Stop'
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw 'GitHub CLI is not installed.' }
& gh auth status
$repos = @('CUMCM-Codex-Workbench','CUMCM-Knowledge-Vault','CUMCM-Contests')
foreach ($repo in $repos) {
    $path = Join-Path $Root $repo
    if (-not (Test-Path $path)) { throw "Missing $path" }
    Push-Location $path
    try {
        if (-not (Test-Path '.git')) { git init }
        git lfs install
        git add .
        git commit -m 'chore: initialize CUMCM repository' 2>$null
        $exists = (& gh repo view $repo --json name 2>$null)
        if (-not $exists) { gh repo create $repo --private --source . --remote origin --push }
        else { Write-Warning "$repo already exists; remote creation skipped." }
    } finally { Pop-Location }
}
