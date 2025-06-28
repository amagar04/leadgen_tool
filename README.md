# Caprae AI LeadGen Tool 🚀

This project was developed as part of Caprae Capital Partners' AI-Readiness Pre-Screening Challenge. It showcases how AI-driven rule-based logic can be used to automate and enhance the B2B lead generation process.

* Objective

To build a lightweight, functional tool within 5 hours that improves the performance of lead prioritization and messaging, aligned with Caprae Capital’s SaaSquatchLeads concept.

*Features

- ✅ Rule-based lead scoring (based on title + description keywords)
- 🔥 Tiered classification (Hot, Warm, Cold)
- 💬 Auto-generated outreach messages for each lead
- 📤 CSV export for use in CRM, email campaigns, or sales pipelines
- Built in **Python** using **Pandas**, compatible with Jupyter and Colab

* Sample Data

Includes a sample `leads.csv` file with fields like:
- Name
- Title
- Company
- Industry
- Email
- About (description)

* Logic Highlights

- 🎯 Title weight: Scores CEOs, Founders, and Heads higher
- 🔍 About analysis: Boosts AI, SaaS, and growth-driven language
- 🧠 Message generation: Creates personalized messages based on tier

* Files Included

- `leadgen_tool.ipynb` – Main notebook
- `leads.csv` – Sample dataset
- `scored_leads_final.csv` – Output with scores, tiers, and messages

* How to Run

1. Upload `leads.csv` or replace with your own
2. Run the notebook in VS Code or Google Colab
3. Export results and use for sales outreach or CRM enrichment

* Future Enhancements

- Streamlit dashboard for drag-and-drop CSV upload
- OpenAI integration for AI-generated messaging
- Live web scraping of contact info

Made by Akanksha Magar
