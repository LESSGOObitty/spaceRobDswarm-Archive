$KE = "C:\spaceRobDswarm\ollama_recycle_orchestrator\recycle_out\kinetic_energy.json"
$Dest = "C:\spaceRobDswarm\telemetry_matrix_map.json"

if (Test-Path $KE) {
    Copy-Item $KE $Dest -Force
}
