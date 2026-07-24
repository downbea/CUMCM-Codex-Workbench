[CmdletBinding()]
param([string]$Root = "D:\obsidian笔记")

$ErrorActionPreference = "Continue"
$report = [ordered]@{}
function Check-Command($name) {
    $cmd = Get-Command $name -ErrorAction SilentlyContinue
    return [ordered]@{ ok = [bool]$cmd; path = if ($cmd) {$cmd.Source} else {$null} }
}

$report.timestamp = (Get-Date).ToString('o')
$report.root = $Root
$report.commands = [ordered]@{
    python = Check-Command 'python'
    git = Check-Command 'git'
    gh = Check-Command 'gh'
    pandoc = Check-Command 'pandoc'
    obsidian = Check-Command 'obsidian'
}
$report.paths = [ordered]@{}
foreach ($name in @('CUMCM-Codex-Workbench','CUMCM-Knowledge-Vault','CUMCM-Contests')) {
    $path = Join-Path $Root $name
    $report.paths[$name] = [ordered]@{ exists = Test-Path $path; writable = $false }
    if (Test-Path $path) {
        try {
            $probe = Join-Path $path '.doctor-write-probe'
            Set-Content -Path $probe -Value 'ok' -Encoding utf8
            Remove-Item $probe -Force
            $report.paths[$name].writable = $true
        } catch {}
    }
}

$word = $null
try {
    $word = New-Object -ComObject Word.Application
    $report.word = [ordered]@{ ok = $true; version = $word.Version }
} catch {
    $report.word = [ordered]@{ ok = $false; error = $_.Exception.Message }
} finally {
    if ($word) { $word.Quit() }
}

try {
    $gpu = Get-CimInstance Win32_VideoController | Select-Object Name, AdapterRAM, DriverVersion
    $report.gpu = @($gpu)
} catch { $report.gpu = @() }
$report.memory_gb = [math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 1)
$report.github_auth = if (Get-Command gh -ErrorAction SilentlyContinue) { (& gh auth status 2>&1 | Out-String) } else { 'gh missing' }

$outDir = Join-Path $PSScriptRoot 'outputs\doctor'
New-Item -ItemType Directory -Path $outDir -Force | Out-Null
$jsonPath = Join-Path $outDir 'doctor-report.json'
$report | ConvertTo-Json -Depth 8 | Set-Content -Path $jsonPath -Encoding utf8
$report | ConvertTo-Json -Depth 8
Write-Host "Saved: $jsonPath" -ForegroundColor Cyan
