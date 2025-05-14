<h1>🐉 Dragon Assistant - Full Setup Instructions</h1>

<p>This guide will walk you through setting up the Dragon Assistant on your Raspberry Pi from scratch.</p>

<hr />

<h2>🧰 What You'll Need</h2>
<ul>
  <li>Raspberry Pi Zero 2 W (or Pi 3/4 for better performance)</li>
  <li>32GB+ microSD card (Class 10 or U1/U3 recommended)</li>
  <li>USB Microphone</li>
  <li>USB Speaker or 3.5mm-powered speaker</li>
  <li>5V 2.5A+ power supply</li>
  <li>Wi-Fi connection</li>
  <li>Computer for flashing the Pi + SSH access</li>
</ul>

<hr />

<h2>📀 Step 1: Flash Raspberry Pi OS Lite (32-bit)</h2>
<ol>
  <li>Download <strong>Raspberry Pi Imager</strong>: <a href="https://www.raspberrypi.com/software">https://www.raspberrypi.com/software</a></li>
  <li>Select OS: <code>Raspberry Pi OS Lite (32-bit)</code></li>
  <li>Choose your microSD card (16–128GB is ideal)</li>
  <li>Click <strong>Advanced Options</strong> (gear icon):
    <ul>
      <li>Enable SSH</li>
      <li>Set hostname (e.g., <code>dragonpi</code>)</li>
      <li>Enter Wi-Fi SSID + password</li>
      <li>Set username to <code>dragon</code>(or whatever you prefer) and password</li>
    </ul>
  </li>
  <li>Flash → Eject → Insert into Pi → Boot!</li>
</ol>

<hr />

<h2>🔗 Step 2: SSH Into Your Pi</h2>

<pre><code>ssh dragon@dragonpi.local</code></pre>

<p>💡 Use your Pi’s IP if .local doesn't resolve. Run <code>ping dragonpi.local</code> or check your router for IP.</p>

<hr />

<h2>🧱 Step 3: Install System Dependencies</h2>

<pre><code>sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git ffmpeg espeak-ng libportaudio2 -y
</code></pre>

<hr />

<h2>🐍 Step 4: Clone the Repo & Set Up Environment</h2>

<pre><code>git clone https://github.com/YOUR_USERNAME/dragon-assistant.git
cd dragon-assistant
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
</code></pre>

<hr />

<h2>🔐 Step 5: Set Up API Keys</h2>

<ol>
  <li>Copy the environment file:</li>
  <pre><code>cp .env.example .env</code></pre>
  <li>Open <code>.env</code> and add your keys:</li>
  <pre><code>OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
PORCUPINE_ACCESS_KEY=your-access-key</code></pre>
  <li>
    <strong>Get your API keys:</strong><br />
    - OpenAI: <a href="https://platform.openai.com/account/api-keys">https://platform.openai.com/account/api-keys</a><br />
    - Porcupine (Picovoice): <a href="https://console.picovoice.ai/">https://console.picovoice.ai/</a>
  </li>
</ol>

<h3>💰 OpenAI Pricing</h3>
<ul>
  <li>gpt-3.5-turbo: ~$0.0015 per 1K input tokens</li>
  <li>gpt-4o: slightly higher, but faster</li>
  <li>TTS: ~$0.015–$0.030 per 1K characters</li>
</ul>
<p><a href="https://platform.openai.com/docs/pricing">Full Pricing Details</a></p>

<hr />

<h2>🔊 Step 6: Add Sound Effects</h2>

<p>Add WAV files to the <code>sounds/</code> directory:</p>
<ul>
  <li><code>wake.wav</code> – after wake word</li>
  <li><code>thinking.wav</code> – after transcribe, before GPT</li>
  <li><code>done.wav</code> – after response spoken</li>
</ul>

<p>You can generate tones with <code>ffmpeg</code>:</p>

<pre><code>ffmpeg -f lavfi -i "sine=frequency=880:duration=0.3" sounds/wake.wav
</code></pre>

<hr />

<h2>🚀 Step 7: Run the Assistant</h2>

<pre><code>source env/bin/activate
python3 main.py
</code></pre>

<p>Speak “Porcupine” → wait for the chime → ask your question → get a spoken response 🎤💬</p>

<hr />

<h2>🧠 Optional Features</h2>
<ul>
  <li>Auto-start with <code>start_dragon.sh</code> + systemd</li>
  <li>Voice command cancel: “cancel”, “nevermind”</li>
  <li>Logs saved in <code>/logs</code> with timestamps</li>
</ul>

<hr />

<h2>🧪 Troubleshooting</h2>

<ul>
  <li><strong>Test microphone:</strong> <code>arecord -l</code></li>
  <li><strong>Test speaker:</strong> <code>aplay -l</code></li>
  <li><strong>Check audio indexing:</strong>
    <pre><code>python3 -c "import sounddevice as sd; print(sd.query_devices())"</code></pre>
  </li>
  <li><strong>Change default speaker:</strong>
    <pre><code>aplay -D plughw:1,0 yourfile.wav</code></pre>
  </li>
</ul>

<hr />

<h2>💡 Want More?</h2>
<ul>
  <li>Run local AI models offline</li>
  <li>Add camera + facial recognition</li>
  <li>Trigger actions via gestures or MQTT</li>
</ul>

<p>Enjoy your hacker-powered, fire-breathing Dragon Assistant 🐲🔥</p>
