[CmdletBinding()]
param([string]$Output = "references\upstream\reports")
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Path $Output -Force | Out-Null
$items = @(
    @{name='nature-skills'; repo='Yuan1z0825/nature-skills'; pinned='91862221b39f7ca16d52ae0e1e9cb6c2bb31a96b'},
    @{name='MathModeling-skills'; repo='zhnnky329/MathModeling-skills'; pinned='50a2942007a98e74cd0948b44d7cb8e4826d15c9'}
)
foreach ($item in $items) {
    $latest = gh api "repos/$($item.repo)/commits/main" --jq '.sha'
    $report = Join-Path $Output "$($item.name)-$(Get-Date -Format yyyyMMdd).md"
    @"
# $($item.name) upstream check

- Repository: https://github.com/$($item.repo)
- Pinned reference: `$($item.pinned)`
- Latest observed: `$latest`
- Status: $(if ($latest -eq $item.pinned) {'no change'} else {'review required'})

No local skill is modified automatically. Ask Codex to compare the two commits and produce a migration proposal before any manual merge.
"@ | Set-Content $report -Encoding utf8
}
