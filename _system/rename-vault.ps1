# Renames the vault D:\Seond brain -> D:\Second brain and fixes everything that uses the old path.
# Close Claude, Obsidian, Word and any Explorer/terminal window inside the vault first.
# Stops without changing anything if the rename fails. -DryRun only lists what would change.
param([switch]$DryRun)
$ErrorActionPreference = 'Stop'
$old = 'D:\Seond brain'; $new = 'D:\Second brain'
$bad = 'Seond brain'; $good = 'Second brain'
$utf8 = New-Object System.Text.UTF8Encoding($false)
$projects = 'C:\Users\User\.claude\projects'
$taskName = 'Obsidian Inbox sync'
Set-Location -LiteralPath 'D:\'

function Fix-Text($path) {
  $t = [IO.File]::ReadAllText($path, $utf8)
  if ($t.Contains($bad) -or $t.Contains('Seond%20brain')) {
    "  fix: $path"
    if (-not $DryRun) { [IO.File]::WriteAllText($path, $t.Replace($bad, $good).Replace('Seond%20brain', 'Second%20brain'), $utf8) }
  }
}

"1. Folder"
if (Test-Path -LiteralPath $new) { throw "$new already exists" }
if ($DryRun) { $root = $old; "  would rename $old -> $new" }
else {
  try { Rename-Item -LiteralPath $old -NewName $good }
  catch { "RENAME FAILED, nothing changed: $($_.Exception.Message)"; "Close the programs using the vault and run this again."; exit 1 }
  $root = $new; "  renamed"
}

"2. Files"
Get-ChildItem -LiteralPath $root -Recurse -File -Force |
  Where-Object { $_.Extension -in '.md', '.py' -and $_.FullName -notmatch '\\\.(obsidian|git|trash)\\' } |
  ForEach-Object { Fix-Text $_.FullName }

"3. Claude memory"
$oldMem = "$projects\D--Seond-brain\memory"; $newDir = "$projects\D--Second-brain"
if (Test-Path -LiteralPath "$newDir\memory") { "  already there, skipped" }
elseif ($DryRun) { "  would copy $oldMem -> $newDir\memory"; Get-ChildItem -LiteralPath $oldMem -File | ForEach-Object { Fix-Text $_.FullName } }
else {
  New-Item -ItemType Directory -Force -Path $newDir | Out-Null
  Copy-Item -LiteralPath $oldMem -Destination "$newDir\memory" -Recurse
  Get-ChildItem -LiteralPath "$newDir\memory" -File | ForEach-Object { Fix-Text $_.FullName }
  "  copied"
}

"4. Scheduled task"
$a = (Get-ScheduledTask -TaskName $taskName).Actions[0]
$args2 = $a.Arguments.Replace($bad, $good); $wd2 = $a.WorkingDirectory.Replace($bad, $good)
"  args: $args2"; "  dir:  $wd2"
if (-not $DryRun) {
  try {
    $n = New-ScheduledTaskAction -Execute $a.Execute -Argument $args2 -WorkingDirectory $wd2
    Set-ScheduledTask -TaskName $taskName -Action $n | Out-Null
    "  updated"
  } catch { "  TASK NOT UPDATED: $($_.Exception.Message)" }
}

"Done. Open $new in Obsidian and start a new Claude session there."
