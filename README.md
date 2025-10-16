# AI Goal Coach

> Your personal AI that builds smart, 7-day goal plans + finds helpful resources from the web!

---

## Overview
AI Goal Coach is a lightweight AI app that helps users **plan and achieve goals** using reasoning + retrieval.

Just type your goal (like *Learn Python* or *Build Muscles*), and the app:
1. Generates a **7-day personalized plan**
2. Fetches **real learning resources**
3. Keeps it simple and motivational 💪

---

## Tech Stack
- **Python**
- **Streamlit** – UI
- **Transformers (HuggingFace)** – AI reasoning model
- **DDGS (DuckDuckGo Search)** – web retrieval for RAG

---

##  Setup

```bash
git clone https://github.com/vishallalwani/AI-Goal-Coach.git
cd AI-Goal-Coach
pip install -r requirements.txt
streamlit run ai_goal_coach.py
