# 📞 Sales Call Analyzer

> An AI-powered sales coaching tool that analyzes call transcripts using the SPIN selling framework — scoring reps across 5 key behaviors and delivering actionable coaching tips in seconds.

---

## 🚀 Live Demo

paste your transcript → get scored → download your report

<img width="960" height="420" alt="KPI" src="https://github.com/user-attachments/assets/1b998fbe-0b10-457f-9957-e0002123bddf" />


---

## 💡 Why I Built This

I spent years working in sales, business development, and customer service. I saw firsthand what separates a great sales call from a poor one — and it's never about the product. It's about listening, building trust, creating urgency, and making the customer feel understood.

Most sales teams don't have time to review every call. Managers can't coach every rep individually. I built this tool to change that — an AI sales coach that reads any call transcript and gives instant, specific, evidence-based feedback.

This is the kind of tool that companies like Gong and Chorus charge $50,000+/year for. I built it from scratch using Python, Streamlit, and the Groq AI API.

---

## ✨ Features

- 🧠 **AI-powered analysis** — scores calls using the globally recognized SPIN selling methodology
- 📊 **5 KPI scorecards** — instant visual scores across key sales behaviors
- 🟢🟡🔴 **Color-coded indicators** — Good, Average, or Needs Work at a glance
- 📋 **Detailed breakdown** — proof from the actual transcript + specific suggestions
- 💡 **Coaching tips** — personalized improvement advice for each rep
- 📥 **Excel export** — downloadable report to share with your team
- 🧪 **Sample transcript** — demo the tool instantly with one click

---

## 📊 Scoring Framework

Built on the **SPIN Selling** methodology by Neil Rackham — one of the most widely used sales frameworks in the world.

| Category | What it measures |
|---|---|
| Open Ended Questions | Does the rep dig deeper with how/what/why questions? |
| Rapport Building | Does the rep connect personally with the customer? |
| Acknowledging Customer | Does the rep reference the customer's own words? |
| Creating Urgency | Does the rep connect the problem to real consequences? |
| Customer Asks for Solution | Is the customer pulling, or is the rep always pushing? |

**Scoring:**
- 🟢 Good — 80% and above
- 🟡 Average — 60% to 79%
- 🔴 Needs Work — below 60%

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core logic and data processing |
| Streamlit | Web interface |
| Groq API (LLaMA 3.3) | AI analysis engine |
| Pandas | Data structuring |
| OpenPyXL | Excel report generation |
| Python-dotenv | Secure API key management |

---

## ⚙️ How to Run It

**1. Clone the repository**
```bash
git clone https://github.com/Amodni007/sales-call-analyzer.git
cd sales-call-analyzer
```

**2. Create a virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
python -m pip install streamlit groq pandas openpyxl python-dotenv
```

**4. Set up your API key**

Create a `.env` file in the project root:
```
GROQ_API_KEY=your-groq-api-key-here
```

Get a free API key at: https://console.groq.com

**5. Run the app**
```bash
streamlit run app.py
```

---

## 📈 Business Impact

- Sales managers can review rep performance **without listening to hours of calls**
- Reps get **specific, evidence-based feedback** — not generic advice
- Coaching becomes **scalable** — one manager can review an entire team's calls
- Built on a **proven global methodology** — not opinions

---

## 🗂️ Project Structure

```
sales-call-analyzer/
│
├── app.py              # Streamlit web interface
├── analyser.py         # AI analysis engine + SPIN prompt
├── .env                # API keys (not uploaded to GitHub)
├── .gitignore          # Protects sensitive files
└── README.md           # You are here
```

---

## 🔮 Future Improvements

- [ ] Upload audio files — auto transcribe with Whisper AI
- [ ] Multi-call comparison dashboard
- [ ] Rep performance tracking over time
- [ ] CRM integration (Salesforce, HubSpot)
- [ ] Custom scoring frameworks per industry

---

## 👤 Built By

**Parul Dhami**  
Sales & Business Development Professional turned Data Analyst

I bring a rare combination of real-world sales experience and technical data skills — I don't just build tools, I build tools that solve problems I've lived firsthand.

🔗 [LinkedIn](https://www.linkedin.com/in/paruldhami/)  
🐙 [GitHub](https://github.com/Amodni007)

---

*If you found this useful, give it a ⭐ on GitHub!*
