# Vault-iig GitHub-d avtomatar backup hiine (Task Scheduler: "Vault backup", odor bur).
# Oorchlolt baival commit, push hiine; ur dung backup.log-d bichne.
$ErrorActionPreference = 'Continue'
$vault = 'D:\Seond brain'
$log = Join-Path $PSScriptRoot 'backup.log'
$env:GIT_TERMINAL_PROMPT = '0'

function Write-Log($msg) {
    "{0}  {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $msg | Out-File -FilePath $log -Append -Encoding utf8
}

Set-Location -LiteralPath $vault
git add -A 2>&1 | Out-Null
$changes = git status --porcelain
if ($changes) {
    $count = @($changes).Count
    git commit -q -m ("auto backup {0} ({1} files)" -f (Get-Date -Format 'yyyy-MM-dd'), $count) 2>&1 | Out-Null
    Write-Log "commit: $count files"
}
$out = git push 2>&1 | Out-String
if ($LASTEXITCODE -eq 0) { Write-Log "push OK" } else { Write-Log ("push FAILED: " + $out.Trim()) }
