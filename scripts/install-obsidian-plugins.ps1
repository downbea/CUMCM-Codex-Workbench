[CmdletBinding()]
param([string]$Vault = "D:\obsidian笔记\CUMCM-Knowledge-Vault")
$ErrorActionPreference = 'Stop'
$plugins = @(
    @{ id='dataview'; repo='blacksmithgu/obsidian-dataview' },
    @{ id='templater-obsidian'; repo='SilentVoid13/Templater' },
    @{ id='obsidian-kanban'; repo='mgmeyers/obsidian-kanban' }
)
$pluginRoot = Join-Path $Vault '.obsidian\plugins'
New-Item -ItemType Directory -Path $pluginRoot -Force | Out-Null
foreach ($p in $plugins) {
    $dest = Join-Path $pluginRoot $p.id
    if (Test-Path $dest) {
        $answer = Read-Host "Plugin $($p.id) exists. Replace it? [y/N]"
        if ($answer -notmatch '^(y|yes)$') { continue }
        Rename-Item $dest "$dest.backup.$(Get-Date -Format yyyyMMddHHmmss)"
    }
    New-Item -ItemType Directory -Path $dest -Force | Out-Null
    $release = Invoke-RestMethod "https://api.github.com/repos/$($p.repo)/releases/latest"
    foreach ($name in @('main.js','manifest.json','styles.css')) {
        $asset = $release.assets | Where-Object { $_.name -eq $name } | Select-Object -First 1
        if ($asset) { Invoke-WebRequest $asset.browser_download_url -OutFile (Join-Path $dest $name) }
    }
}
Write-Host 'Obsidian community plugins installed. Enable them after reviewing Restricted Mode.'
