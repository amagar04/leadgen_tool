
# Caprae AI Lead Scorer — Project Report

### 🚀 Objective
To build an AI-enhanced lead scoring tool that analyzes business descriptions (“About”) and ranks them based on relevance using NLP.

### 🧠 Technical Stack
- **TF-IDF** (from scikit-learn) to score how content-rich or signal-rich each lead's “About” section is
- **Streamlit** to allow CSV upload, scoring, viewing, and downloading

### 💼 Business Relevance
The tool mimics how a human would scan profiles and prioritize outreach — ideal for sales, VC analysts, or growth teams.

### 📊 Output
Each lead is tagged as:
- 🔥 Hot (Top opportunity)
- ⚡ Warm (Potential lead)
- ❄️ Cold (Low value/unclear signal)

### 🛠️ Future Plans
- Switch to LLM-based understanding
- Enrich data with LinkedIn/email status
- CRM export templates (HubSpot/Salesforce)
