$ErrorActionPreference = "SilentlyContinue"

$Root = "C:\spaceRobDswarm"
$Orch = Join-Path $Root "ollama_recycle_orchestrator"
$Manifest = Join-Path $Orch "manifest.json"

$Targets = (Get-Content $Manifest | ConvertFrom-Json).targets

# Operator cycle: 3600 seconds
$CycleSeconds = 3600

while ($true) {

    Write-Host "[RE-CYCLE] Starting new operator cycle..."

    foreach ($t in $Targets) {
        $Path = Join-Path $Root $t

        Write-Host "[HARVEST] $Path"
        python "$Orch\reducer.py" --file "$Path"

        Write-Host "[RECYCLE] $Path"
        python "$Orch\recycler.py" --file "$Path"

        Write-Host "[RE-EMIT] $Path"
        python "$Orch\emitter.py" --file "$Path"
    }

    Write-Host "[KINETIC] Computing swarm kinetic energy..."
    python "$Orch\kinetic_energy.py"

    Write-Host "[RE-CYCLE] Cycle complete. Sleeping $CycleSeconds seconds."
    Start-Sleep -Seconds $CycleSeconds
}
