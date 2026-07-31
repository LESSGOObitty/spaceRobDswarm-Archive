import time
import math
import random
from datetime import datetime
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)
TOTAL_MONOLITH_CYCLES = 0
START_TIME_EPOCH = time.time()

def calculate_ehf_biometrics():
    global TOTAL_MONOLITH_CYCLES
    m = (TOTAL_MONOLITH_CYCLES % 24) + 1
    tau_tick = m / 7200.0
    
    # Flat mathematical equations tracking the continuous circadian curves
    hr = 65.0 + 5.0 * math.sin(2 * math.pi * tau_tick) + random.uniform(-2, 2)
    hrv = 70.0 + 10.0 * math.cos(2 * math.pi * tau_tick) + random.uniform(-3, 3)
    stress_score = 20.0 + 8.0 * math.sin(2 * math.pi * tau_tick) + random.uniform(-2, 2)
    cortisol = 15.2 + 4.5 * math.sin(2 * math.pi * tau_tick)
    glucose = 92.4 + 5.0 * math.cos(2 * math.pi * tau_tick)
    
    # Pure evaluation mapping based on clock ticks without conditional string matching
    states = ["PEAK_FOCUS", "DEEP_WORK", "CREATIVE", "RELAXED"]
    state = states[m % 4]
    freq = 6.0 if state == "DEEP_WORK" else (10.0 if state == "PEAK_FOCUS" else 20.0)
        
    human_readiness = random.uniform(85, 99)
    tron_consensus = random.uniform(92, 99)
    combined_readiness = (human_readiness * tron_consensus) / 100.0
    
    return m, tau_tick, state, freq, hr, hrv, stress_score, cortisol, glucose, combined_readiness

@app.route('/data')
def get_live_data():
    global TOTAL_MONOLITH_CYCLES
    m, tau, state, freq, hr, hrv, stress, cort, gluc, ready = calculate_ehf_biometrics()
    TOTAL_MONOLITH_CYCLES += 1
    return jsonify(
        cycles=TOTAL_MONOLITH_CYCLES,
        m=m,
        tau=f"{tau:.6f}",
        state=state,
        freq=freq,
        hr=f"{hr:.1f}",
        hrv=f"{hrv:.1f}",
        stress=f"{stress:.1f}",
        cort=f"{cort:.2f}",
        gluc=f"{gluc:.1f}",
        ready=f"{ready:.2f}%"
    )

@app.route('/')
def home():
    return render_template_string('''
    <html>
    <head>
        <title>ROBDOE.COM // ULTRA HYPERSPACE CORE</title>
        <style>
            body { background-color: #000; color: #00ff00; font-family: monospace; font-size: 16px; padding: 30px; }
            .crt-frame { border: 2px solid #00ff00; padding: 20px; border-radius: 5px; box-shadow: 0 0 25px rgba(0,255,0,0.6); line-height: 1.6; }
            .highlight { color: #ff00ff; font-weight: bold; text-shadow: 0 0 10px #ff00ff; }
            .val { color: #ffff00; font-weight: bold; }
        </style>
        <script>
            function refreshEHF() {
                fetch('/data')
                    .then(r => r.json())
                    .then(data => {
                        document.getElementById('header').innerHTML = `┌──────────────────────────────────────────────────────────────────┐<br>│ ⚡ ROBDOE.COM // ENGINE RUNNING IN HIGH-FREQUENCY HYPERSPACE LOOP │<br>└──────────────────────────────────────────────────────────────────┘`;
                        
                        let body = `<b>TIER 0: BIOMETRIC INTENT CONVERGENCE (MAX SPEED TUNING)</b><br>` +
                                   ` ├─ ENGINE STATUS : <span style="color:black; background:#00ff00; font-weight:bold; padding:2px;">HYPER_DRIVE</span> &nbsp;|&nbsp; REFRESH RATE: 50ms (20Hz)<br>` +
                                   ` ├─ SYSTEM CYCLE  : <span class="val">${String(data.cycles).padStart(6, '0')}</span> &nbsp;|&nbsp; τ-TICK INTERVAL: ${data.tau}<br>` +
                                   ` ├─ CURRENT STATE : <span style="color:yellow; font-weight:bold;">${data.state}</span> (${data.freq} Hz Phase Lock)<br>` +
                                   ` ├─ SYSTEM READINESS COMBINATOR : <span class="highlight">${data.ready}</span> (PROCEED FORWARD)<br>` +
                                   `--------------------------------------------------------------------<br>` +
                                   `<b>BIOMARKER INGESTION ARRAY (CONTINUOUS MULTI-NODE TELEMETRY):</b><br>` +
                                   ` &nbsp;▶ HEART RATE &nbsp; &nbsp; &nbsp; &nbsp;: ${data.hr} BPM &nbsp; &nbsp; &nbsp; &nbsp;▶ HRV MATRIX &nbsp;: ${data.hrv} ms<br>` +
                                   ` &nbsp;▶ CORTISOL DYNAMICS : ${data.cort} ng/mL &nbsp; &nbsp; &nbsp;▶ GLUCOSE TRACKER: ${data.gluc} mg/dL<br>` +
                                   ` &nbsp;▶ STRESS SPECTRUM &nbsp; : ${data.stress}/100<br>` +
                                   `--------------------------------------------------------------------<br>` +
                                   `<span style="color:#00ffff;"><b>[CONTINENTAL_SWARM]</b> 19-NODES ALIGNED // NEM + WEM + NT INTERFACES ACTIVE</span><br>` +
                                   `FLOWING PURE KINETIC INTENT BACKED BY C:\\awesomerobdoe-green-software.robdoe`;
                        document.getElementById('header').style.display = 'block';
                        document.getElementById('body').innerHTML = body;
                    });
            }
            setInterval(refreshEHF, 50); 
            window.onload = refreshEHF;
        </script>
    </head>
    <body>
        <div class="crt-frame">
            <div id="header">Initializing Hyper-Drive Sockets...</div>
            <br>
            <div id="body">Deploying streaming vectors...</div>
        </div>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    import os
    port = 8002
    if "NEMOSIS" in os.getcwd(): port = 8000
    elif "NEMSEER" in os.getcwd(): port = 8001
    app.run(host='0.0.0.0', port=port, debug=False)
