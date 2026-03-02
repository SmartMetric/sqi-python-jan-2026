while ($true) {
    git add -A

    $changes = git status --porcelain
    if ($changes) {
        $time = Get-Date -Format "yyyy-MM-dd HH:mm"
        git commit -m "auto update $time"
        git push
    }

    Start-Sleep -Seconds 300
}Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
