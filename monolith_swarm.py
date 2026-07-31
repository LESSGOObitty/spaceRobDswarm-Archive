import time
import math
import random
from datetime import datetime
import threading
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)
TOTAL_MONOLITH_CYCLES = 0
START_TIME_EPOCH = time.time()

def calculate_swarm_wave_mechanics():
    global TOTAL_MONOLITH_CYCLES
    m = (TOTAL_MONOLITH_CYCLES % 24) + 1
    tau_tick = m / 7200.0
    
    dPhi_dt = random.uniform(-15.5, 15.5)
    rho_k = random.uniform(85.4, 99.1)
    
    mu_0 = 1.256e-6
    sigma_k = 5.8e7  
    alpha_K = 0.05   
    
    psi_gamma = (mu_0 * sigma_k * dPhi_dt) + (alpha_K * math.sin(2 * math.pi * tau_tick)) + (rho_k * 0.01)
    
    # Track the pattern that emerges when intent rhythm nodes engage
    # Engages when the 1/7200 interval train hits pure integer divisions
    rhythm_node_active = "ACTIVE" if (m % 6 == 0) else "IDLE"
    rhythm_resonance = math.cos(2 * math.pi * tau_tick) * 0.05 if rhythm_node_active == "ACTIVE" else 0.0
    
    freq_deviation = random.uniform(-0.05, 0.05) 
    df_dt = random.uniform(-0.02, 0.02)
    K_f = 12.5  
    K_p = 25.0  
    P_inj = -(K_f * df_dt) - (K_p * freq_deviation) + rhythm_resonance
    
    return m, tau_tick, dPhi_dt, rho_k, psi_gamma, P_inj, rhythm_node_active

@app.route('/data')
def get_live_data():
    global TOTAL_MONOLITH_CYCLES
    m, tau, dPhi, rho, psi, p_inj, rhythm_state = calculate_swarm_wave_mechanics()
    TOTAL_MONOLITH_CYCLES += 1
    return jsonify(
        cycles=TOTAL_MONOLITH_CYCLES,
        m=m,
        tau=f"{tau:.6f}",
        psi=f"{psi:+.6f}",
        dphi=f"{dPhi:+.4f}",
        rho=f"{rho:.2f}",
        pinj=f"{p_inj:+.4f}",
        rhythm=rhythm_state,
        time=datetime.now().strftime('%H:%M:%S.%f')[:-4]
    )

@app.route('/')
def home():
    return render_template_string('''
    <html>
    <head>
        <title>ROBDOE.COM // INTENT RHYTHM MATRIX</title>
        <style>
            body { background-color: #000; color: #00ff00; font-family: monospace; font-size: 18px; padding: 30px; }
            .crt-frame { border: 2px solid #00ff00; padding: 20px; border-radius: 5px; box-shadow: 0 0 15px rgba(0,255,0,0.4); line-height: 1.6; }
            .highlight { color: #ff00ff; font-weight: bold; }
            .val { color: #ffff00; font-weight: bold; }
            .active-node { color: #00ffff; font-weight: bold; text-shadow: 0 0 8px #00ffff; }
        </style>
        <script>
            function fetchTelemetry() {
                fetch('/data')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('matrix_header').innerHTML = `⚙ <span class="highlight">ROBDOE.COM</span> // INTENT RHYTHM NODE PULSE MONITOR`;
                        document.getElementById('clock_line').innerHTML = `CLOCK CYCLE: ${String(data.cycles).padStart(6, '0')} &nbsp;| &nbsp;TRAIN STEP [m]: ${String(data.m).padStart(2, '0')}/24 &nbsp;| &nbsp;τ-TICK: ${data.tau}`;
                        
                        let rhythmStatus = data.rhythm === "ACTIVE" 
                            ? `<span class="active-node">▲ ACTIVE HARMONIC RESONANCE CONVERGENCE detected</span>` 
                            : `<span style="color: #555555;">▼ IDLE_INTERVAL_ALIGNMENT</span>`;

                        let body = `[<span style="color: #ff0000;">CHAKRA_01</span>] WAVE PHASE ANGLE (Ψ_γ) : <span class="val">${data.psi} rad</span><br>` +
                                   `[<span style="color: #ff7f00;">CHAKRA_02</span>] POWER FLUX SHIFT (∂Φ/∂t): <span style="color: #00ffff; font-weight:bold;">${data.dphi} MW/s</span><br>` +
                                   `[<span style="color: #00ff00;">CHAKRA_04</span>] INVERTER MATCHING (P_inj): <span class="val">${data.pinj} MW</span><br>` +
                                   `------------------------------------------------------------------------------------------<br>` +
                                   `RHYTHM NODE VECTOR STATUS: ${rhythmStatus}<br>` +
                                   `------------------------------------------------------------------------------------------<br>` +
                                   `HYDREN SYSTEM MAP (7D HEXAGON RECYCLE FRAMEWORK):<br>` +
                                   ` ⭕ TOP LAYER &nbsp; [2 CIRCLES] : GEOMETRIC INTENT LOCK<br>` +
                                   ` ⭕ MID LAYER &nbsp; [3 CIRCLES] : TETRA.4D CLOCK BALANCER ACTIVE<br>` +
                                   ` ⭕ BASE LAYER [2 CIRCLES] : HEDRA.3D 0-POWER MANIFEST SECURE<br>` +
                                   `------------------------------------------------------------------------------------------<br>` +
                                   `<span style="color: #0000ff; font-weight:bold;">[KINETIC_IDLE]</span> CORE LOG PATTERN STABLE // PROCESSED AT SYNC TIME: ${data.time}`;
                        document.getElementById('matrix_body').innerHTML = body;
                    });
            }
            setInterval(fetchTelemetry, 400); 
            window.onload = fetchTelemetry;
        </script>
    </head>
    <body>
        <div class="crt-frame">
            <div id="matrix_header">Awaiting signal connection...</div>
            <div>==========================================================================================</div>
            <div id="clock_line">Calibrating interval clock...</div>
            <div>==========================================================================================</div>
            <br>
            <div id="matrix_body">Tracking rhythm node engagement vector...</div>
        </div>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    # Configured to dynamic execution deployment ports
    import sys
    port = 8000
    if "NEMSEER" in os.getcwd(): port = 8001
    elif "spaceRobDswarm" in os.getcwd(): port = 8002
    import os
    app.run(host='0.0.0.0', port=port, debug=False)
