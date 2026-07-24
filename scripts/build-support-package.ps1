[CmdletBinding()]
param(
  [Parameter(Mandatory=$true)][string]$Project,
  [string]$OutputZip
)
$ErrorActionPreference='Stop'
$Project=[IO.Path]::GetFullPath($Project)
if (-not $OutputZip) { $OutputZip=Join-Path $Project 'deliverables\CUMCM-support-materials.zip' }
$OutputZip=[IO.Path]::GetFullPath($OutputZip)
$required=@('paper','support-materials','audits','project_state.json','decision_log.md')
foreach ($r in $required) { if (-not (Test-Path (Join-Path $Project $r))) { throw "Missing required path: $r" } }
$state=Get-Content (Join-Path $Project 'project_state.json') -Raw | ConvertFrom-Json
if ($state.gates.results_frozen -ne 'APPROVED') { throw 'Results are not frozen.' }
if ($state.gates.logic_audit -notin @('APPROVED','RISK_ACCEPTED')) { throw 'Logic audit gate is not released.' }
if ($state.gates.consistency_audit -notin @('APPROVED','RISK_ACCEPTED')) { throw 'Consistency audit gate is not released.' }
if ($state.gates.compliance_audit -notin @('APPROVED','RISK_ACCEPTED')) { throw 'Compliance audit gate is not released.' }
New-Item -ItemType Directory -Path (Split-Path $OutputZip -Parent) -Force | Out-Null
if (Test-Path $OutputZip) {
  $answer=Read-Host "Output exists. Back up and replace it? [y/N]"
  if ($answer -notmatch '^(y|yes)$') { exit 1 }
  Move-Item $OutputZip "$OutputZip.backup.$(Get-Date -Format yyyyMMddHHmmss)"
}
$items=@()
foreach ($r in $required) { $items += Join-Path $Project $r }
Compress-Archive -Path $items -DestinationPath $OutputZip -CompressionLevel Optimal
Write-Host "Created $OutputZip"
