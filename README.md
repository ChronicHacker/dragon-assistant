<h1>🐉 Dragon Assistant</h1>

<p>A blazing-fast voice assistant for Raspberry Pi powered by OpenAI GPT and Picovoice Porcupine.</p>

<blockquote>
  Say the wake word (“Porcupine”) and ask your question. Dragon transcribes your speech, generates a smart reply using GPT-3.5 or GPT-4o, and responds out loud using OpenAI’s TTS. Comes with audio cues, cancel command support, and full logging.
</blockquote>

<h2>🚀 Features</h2>
<ul>
  <li>🦔 Wake word detection with <strong>Porcupine</strong> (“Porcupine”)</li>
  <li>🎙️ Voice input → transcribed with OpenAI Whisper</li>
  <li>🧠 Smart replies via <strong>GPT-3.5-Turbo</strong> or <strong>GPT-4o</strong></li>
  <li>🔊 Spoken responses with <strong>OpenAI TTS</strong> (<code>shimmer</code>, <code>nova</code>, etc.)</li>
  <li>💬 Cancel with natural voice commands (“nevermind”, “cancel”, etc.)</li>
  <li>🔔 Confirmation, thinking, and “done speaking” chimes</li>
  <li>📁 Each interaction saved in <code>/logs/</code> with timestamped <code>.txt</code> files</li>
  <li>✅ Fully headless — works over SSH on <strong>Raspberry Pi OS Lite (32-bit)</strong></li>
</ul>

<h2>🧪 Requirements</h2>
<ul>
  <li>Raspberry Pi Zero 2 W, Pi 3, or Pi 4</li>
  <li>USB mic + USB speaker</li>
  <li>Python 3.11+</li>
  <li>API keys from OpenAI & Picovoice</li>
</ul>

<h2>📦 Quick Start</h2>
<pre><code>git clone https://github.com/yourusername/dragon-assistant.git
cd dragon-assistant
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add your keys
python3 main.py
</code></pre>

<h2>📖 Full Setup Instructions</h2>
<p>See <code><a href="./INSTRUCTIONS.md">INSTRUCTIONS.md</a></code> for step-by-step guidance on:</p>
<ul>
  <li>Flashing Raspberry Pi OS Lite</li>
  <li>Installing dependencies</li>
  <li>Configuring <code>.env</code> and sound effects</li>
  <li>Running &amp; auto-starting the assistant</li>
</ul>

<h2>💰 API Pricing</h2>
<p>
  OpenAI API usage is pay-as-you-go.<br />
  See pricing details here → 
  <a href="https://platform.openai.com/docs/pricing" target="_blank">OpenAI Pricing</a>
</p>
