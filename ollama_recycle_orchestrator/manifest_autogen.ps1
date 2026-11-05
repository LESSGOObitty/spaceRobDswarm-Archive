$Root = "C:\spaceRobDswarm"
$Manifest = "$Root\ollama_recycle_orchestrator\manifest.json"

$targets = @(
    "src",
    "docs",
    "monolith_swarm.py"
)

$matrices = Get-ChildItem $Root -Filter "*matrix.json" | ForEach-Object { $_.Name }

$full = @{
    targets = $targets + $matrices
}

$full | ConvertTo-Json -Depth 5 | Set-Content $Manifest
