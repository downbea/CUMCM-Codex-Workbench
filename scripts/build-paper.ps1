[CmdletBinding()]
param(
  [Parameter(Mandatory=$true)][string]$Markdown,
  [string]$OutputDocx,
  [string]$OutputPdf,
  [string]$ReferenceDocx = "$PSScriptRoot\..\templates\word\CUMCM_reference_template.docx",
  [string]$Bibliography
)
$ErrorActionPreference = 'Stop'
$Markdown = [IO.Path]::GetFullPath($Markdown)
if (-not $OutputDocx) { $OutputDocx = [IO.Path]::ChangeExtension($Markdown, '.docx') }
if (-not $OutputPdf) { $OutputPdf = [IO.Path]::ChangeExtension($Markdown, '.pdf') }
$OutputDocx = [IO.Path]::GetFullPath($OutputDocx)
$OutputPdf = [IO.Path]::GetFullPath($OutputPdf)
$ReferenceDocx = [IO.Path]::GetFullPath($ReferenceDocx)
$assembled = [IO.Path]::ChangeExtension($OutputDocx, '.assembled.md')

& "$PSScriptRoot\..\.venv\Scripts\python.exe" -m cummcm_workbench.cli assemble-paper $Markdown $assembled
$args = @($assembled,'--from','markdown+tex_math_dollars','--reference-doc',$ReferenceDocx,'--standalone','--toc','-o',$OutputDocx)
if ($Bibliography) { $args += @('--citeproc','--bibliography',[IO.Path]::GetFullPath($Bibliography)) }
& pandoc @args

$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($OutputDocx)
    foreach ($field in $doc.Fields) { $field.Update() | Out-Null }
    foreach ($toc in $doc.TablesOfContents) { $toc.Update() }
    $doc.Save()
    $doc.ExportAsFixedFormat($OutputPdf, 17)
    $doc.Close()
} finally { $word.Quit() }
Write-Host "Built $OutputDocx and $OutputPdf"
