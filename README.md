# 🧙‍♂️ RPG Adventure Web App (Narrated by LLaMA 3.1)

Welcome to **RPG Adventure**, a web-based role-playing game powered by LLaMA 3.1 through Ollama and built with Python Flask. This application lets players engage with an AI narrator who guides them through a fantasy storyline full of choices.

## 📖 About the Project

This project allows players to participate in a branching narrative RPG game where each chapter ends with 4 choices. The AI (LLaMA 3.1) acts as the narrator and story generator.

The system:
- Creates immersive story chapters
- Presents 4 choices at each step (1–4)
- Validates inputs and handles invalid responses gracefully
- Remembers recent conversation history for coherence
- Runs a Flask backend with memory endpoints and a styled frontend

## 🛠️ Technologies Used

| Tech              | Role                                    |
|-------------------|------------------------------------------|
| Python Flask      | Backend API server                       |
| HTML/CSS/JS       | Frontend user interface                  |
| Ollama            | LLaMA 3.1 model execution                |
| Deque (collections)| In-memory chat history management      |

## 📦 Folder Structure




## 🚀 Features

- 🎮 **Interactive Story Mode**: Engage in a live RPG narrative with choices at every turn.
- 🧠 **Contextual Memory**: Keeps track of the last 30 messages for dynamic storytelling.
- 🧹 **Memory Tools**:
  - `GET /api/memory/status` – Check memory usage
  - `POST /api/memory/clear` – Reset conversation history
  - `GET /api/memory/export` – Export past interactions
- 💬 **Error Handling**: Detects and handles invalid choices gracefully.
- ✨ **Responsive UI**: Aesthetically styled HTML/CSS layout with animations and mobile-friendly design.

## 🔧 Installation & Usage

### Requirements
- Python 3.10+
- Ollama installed locally with `llama3.1` model available
- Flask

### Setup

```
git clone https://github.com/Erdem_Daud/RPG-game-in_LLM.git
cd RPG_game_in_LLM
pip install flask
ollama run llama3.1
python receiver.py
