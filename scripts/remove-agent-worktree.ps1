[CmdletBinding()]
param([Parameter(Mandatory=$true)][string]$Path)
$answer=Read-Host "Remove worktree $Path? Uncommitted changes may be lost. [y/N]"
if ($answer -notmatch '^(y|yes)$') { exit 1 }
git -C $Path status --short
git worktree remove $Path
