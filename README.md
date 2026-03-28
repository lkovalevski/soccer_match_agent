# ⚽ Football Agent — Newell's Match Analyzer

An AI agent that fetches sports news articles and produces structured pre-match analyses for Newell's Old Boys, built using the **GAME framework** (Goal – Actions – Memory – Environment).

---

## 🧠 Architecture: GAME Framework

This project applies the GAME design pattern for AI agents:

| Component | Description |
|-----------|-------------|
| **Goal** | What the agent wants to achieve — analyze an article and produce a pre-match report |
| **Actions** | The tools available to the agent — fetch, extract, summarize, terminate |
| **Memory** | A record of what the agent has done during its execution loop |
| **Environment** | The context the agent operates in — web articles, LLM responses |

---

## 📁 Project Structure

```
football_agent/
│
├── main.py                     ← Entry point. Runs the agent.
├── config.py                   ← API keys and model settings
│
├── agent/
│   ├── goals.py                ← Defines the agent's goals (GAME: Goal)
│   ├── tools.py                ← Tool functions the agent can call (GAME: Actions)
│   └── agent_setup.py          ← Assembles the agent with all components
│
├── framework/
│   └── game_framework.py       ← Base GAME framework (Agent, Goal, Memory, Environment)
│
├── requirements.txt            ← Python dependencies
└── README.md                   ← This file
```

---

## 🔄 Agent Flow

```
main.py
  └── creates agent (agent_setup.py)
        └── with goals (goals.py)
        └── with tools (tools.py)
              ├── fetch_article(url)         → fetches raw HTML
              ├── extract_main_text(html)    → cleans and extracts readable text
              ├── summarize_match_outlook(text) → GPT-4o structured analysis
              └── terminate(message)         → ends execution, returns final report
```

The agent runs in a loop, selecting tools based on its goals, until it calls `terminate`.

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/lkovalevski/soccer_match_agent.git
cd soccer_match_agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key

```bash
# macOS/Linux
export OPENAI_API_KEY="sk-..."

# Windows CMD
set OPENAI_API_KEY="sk-..."
```

> ⚠️ Never hardcode your API key in the source code. Add `config.py` to `.gitignore` if you store the key there directly.

### 5. Run the agent

```bash
python main.py
```

---

## 📊 Output Example

```
============================================================
FINAL REPORT
============================================================

1. Current Team Situation
   Newell's has had a difficult start to the season...

2. Strengths
   Strong defensive organization and set pieces...

3. Weaknesses
   Lack of creativity in midfield...

4. Tactical Outlook
   Likely to sit deep and hit on the counter...

5. Psychological Context
   Pressure from fans after a string of poor results...

6. Expected Match Scenario
   A tight, low-scoring game with Newell's looking to avoid defeat...
```

---

## 🔧 Configuration

Edit `config.py` to change the model or default article URL:

```python
MODEL = "openai/gpt-4o"       # or "openai/gpt-4-turbo", etc.
MAX_TOKENS = 800
DEFAULT_ARTICLE_URL = "https://..."
```

---

## 🚀 Roadmap

- [x] Single source article analysis (rosario3)
- [ ] Multiple source aggregation
- [ ] Twitter/X analyst sentiment scraping
- [ ] Historical match metrics integration
- [ ] Probabilistic win/draw/loss prediction
- [ ] Web UI or Telegram bot interface

---

## 📚 Concepts Covered

- GAME framework for agent design
- Tool registration and function calling
- Web scraping with `requests` + `BeautifulSoup`
- LLM integration via `litellm`
- Agent memory and execution loop

---

## 📄 License

MIT
