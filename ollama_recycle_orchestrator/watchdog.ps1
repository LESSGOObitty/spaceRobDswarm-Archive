$task = "SwarmRecycleOrchestrator"

while ($true) {
    $status = schtasks /query /tn $task | Select-String "Running"

    if (-not $status) {
        schtasks /run /tn $task
    }

    Start-Sleep -Seconds 30
}
