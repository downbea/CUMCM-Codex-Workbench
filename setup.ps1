[CmdletBinding(SupportsShouldProcess=$true)]
param(
    [string]$Root = "D:\obsidian笔记",
    [switch]$InstallAdvanced,
    [switch]$CreateGitHubRepos
)

$ErrorActionPreference = "Stop"
$Workbench = Join-Path $Root "CUMCM-Codex-Workbench"
$Vault = Join-Path $Root "CUMCM-Knowledge-Vault"
$Contests = Join-Path $Root "CUMCM-Contests"

function Require-Confirmation([string]$Message) {
    $answer = Read-Host "$Message [y/N]"
    return $answer -match '^(y|yes)$'
}

Write-Host "CUMCM Workbench setup" -ForegroundColor Cyan
Write-Host "Root: $Root"

$packages = @(
    @{Name='Git.Git'; Command='git'},
    @{Name='GitHub.cli'; Command='gh'},
    @{Name='Python.Python.3.12'; Command='python'},
    @{Name='JohnMacFarlane.Pandoc'; Command='pandoc'},
    @{Name='Obsidian.Obsidian'; Command='obsidian'}
)

foreach ($pkg in $packages) {
    if (-not (Get-Command $pkg.Command -ErrorAction SilentlyContinue)) {
        if (Require-Confirmation "Install $($pkg.Name) with winget?") {
            winget install --id $pkg.Name --exact --accept-package-agreements --accept-source-agreements
        } else {
            Write-Warning "$($pkg.Command) is missing. doctor.ps1 will report it."
        }
    }
}

if (-not (Get-Command git-lfs -ErrorAction SilentlyContinue)) {
    if (Require-Confirmation "Install Git LFS with winget?") {
        winget install --id GitHub.GitLFS --exact --accept-package-agreements --accept-source-agreements
    }
}

foreach ($dir in @($Root,$Workbench,$Vault,$Contests)) {
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
}

if ((Resolve-Path $PSScriptRoot).Path -ne (Resolve-Path $Workbench).Path) {
    Write-Warning "The script is not running from $Workbench. Copy the delivered Workbench directory there before continuing."
}

Set-Location $PSScriptRoot
if (-not (Test-Path '.venv')) { python -m venv .venv }
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements-core.txt
if ($InstallAdvanced) {
    & .\.venv\Scripts\python.exe -m pip install -r requirements-advanced.txt
}

if (Get-Command git -ErrorAction SilentlyContinue) {
    git lfs install
    if (-not (Test-Path '.git')) { git init }
}

$launcherSource = Join-Path $PSScriptRoot 'launcher-skill\cummcm-workbench-launcher'
$launcherDest = Join-Path $HOME '.codex\skills\cummcm-workbench-launcher'
New-Item -ItemType Directory -Path (Split-Path $launcherDest) -Force | Out-Null
if (Test-Path $launcherDest) {
    if (Require-Confirmation "Replace existing global launcher at $launcherDest?") {
        $backup = "$launcherDest.backup.$(Get-Date -Format yyyyMMddHHmmss)"
        Move-Item $launcherDest $backup
        Copy-Item $launcherSource $launcherDest -Recurse
    }
} else {
    Copy-Item $launcherSource $launcherDest -Recurse
}

if ($CreateGitHubRepos) {
    & (Join-Path $PSScriptRoot 'scripts\create-private-repos.ps1') -Root $Root
}

Write-Host "Setup complete. Run .\doctor.ps1 next." -ForegroundColor Green
