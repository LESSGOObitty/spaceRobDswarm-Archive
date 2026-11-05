$models = @("llama3:latest", "phi3:latest", "llama3:8b")
$indexFile = "C:\spaceRobDswarm\ollama_recycle_orchestrator\model_index.txt"

if (-not (Test-Path $indexFile)) {
    "0" | Set-Content $indexFile
}

$index = [int](Get-Content $indexFile)
$model = $models[$index]

$model | Set-Content "C:\spaceRobDswarm\ollama_recycle_orchestrator\active_model.txt"

$next = ($index + 1) % $models.Count
$next | Set-Content $indexFile
