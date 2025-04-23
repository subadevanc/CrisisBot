# 🛡️ CrisisBot – Offline Simple Agent for Disaster Zones Prototype

> Helping people in disaster zones when the internet fails. Runs fully offline and works even on mobile via local Wi-Fi.

---

## 🚨 What is CrisisBot?

**CrisisBot** is a lightweight, offline-capable AI chatbot built using Python and Flask. It can assist individuals during emergencies — like natural disasters — where network connectivity is down.

Whether it’s asking for **water**, **location help**, or simply sending distress messages, CrisisBot listens and responds with basic AI logic and optional voice feedback using Text-to-Speech.

---

## 🌟 Features

- ✅ **Offline Capable** – No internet required
- 📱 **Mobile-Accessible** – Connect via hotspot/local IP
- 🗣️ **Text-to-Speech** using `pyttsx3`
- 💡 Smart keyword-based responses
- 🧠 Easy to expand with more logic or AI models

---

## 🔧 Tech Stack

- **Python 3**
- **Flask** – lightweight web server
- **HTML** – minimal front-end
- **pyttsx3** – offline TTS (Text to Speech)

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

> You can generate this with:
> `pip freeze > requirements.txt`

Example contents:

```
Flask==2.2.5
pyttsx3==2.90
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/subadevanc/CrisisBot.git
   cd CrisisBot
   ```

2. Start the Flask server:
   ```bash
   python3 crisisbot.py
   ```

3. Open your browser and go to:

   ```
   http://localhost:5000
   ```

4. To access from mobile:
   - Connect your phone and laptop to the same Wi-Fi / hotspot
   - Find your laptop's IP:
     ```bash
     ip addr show
     ```
   - Visit `http://<your-laptop-ip>:5000` on mobile browser

---

## 🧠 How It Works

- Flask receives your message
- CrisisBot echoes back with an "Acknowledged ->" prefix
- If `pyttsx3` is installed, it speaks the message aloud
- All chat is stored in memory for now (can be improved with SQLite)

---

## 📁 File Structure

```
CrisisBot/
├── templates/
│   └── index.html         # Front-end UI
├── crisisbot.py           # Main server
├── requirements.txt       # Python dependencies
└── README.md              # Project info
```

---

## 🙋‍♂️ Made By

**Subadevan C**  
🎓 2nd Year CSE | Jerusalem College of Engineering  
🎯 Cybersecurity Enthusiast | Hackathon Competitor | CTF Player  
🔗 GitHub: [@subadevanc](https://github.com/subadevanc)

---

## 📌 To-Do (Ideas to Improve)

- [ ] Add chatbot memory (store conversation)# 🛡️ CrisisBot – Offline AI Agent for Disaster Zones



## 🙋‍♂️ Made By

**Subadevan C**  
🎓 2nd Year CSE | Jerusalem College of Engineering  
🎯 Cybersecurity Enthusiast | Hackathon Competitor | CTF Player  
🔗 GitHub: [@subadevanc](https://github.com/subadevanc)

---

## 📌 To-Do (Ideas to Improve)

- [ ] Add chatbot memory (store conversation)
- [ ] Add SQLite database for logging
- [ ] Expand AI logic (e.g., detect "injury", "fire", "lost", etc.)
- [ ] Voice input (speech-to-text)
- [ ] Package as Android APK using Kivy or BeeWare

---

## 🆘 License

MIT License – use it, fork it, improve it! Stay safe out there 🌍

- [ ] Add SQLite database for logging
- [ ] Expand AI logic (e.g., detect "injury", "fire", "lost", etc.)
- [ ] Voice input (speech-to-text)
- [ ] Package as Android APK using Kivy or BeeWare
- [ ] Integrate LoRa Modules for long-range offline communication
---
