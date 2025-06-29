
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

st.set_page_config(page_title="Caprae AI Lead Scorer", layout="wide")
st.title("🧠 Caprae Lead Scorer (AI Enhanced)")

uploaded_file = st.file_uploader("📤 Upload your leads.csv file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['About'] = df['About'].fillna('')

    # Apply TF-IDF scoring
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['About'])
    df['TFIDF_Score'] = tfidf_matrix.mean(axis=1).A1

    # Define tiering logic
    def assign_tier(score):
        if score > 0.05:
            return "🔥 Hot Lead"
        elif score > 0.02:
            return "⚡ Warm Lead"
        else:
            return "❄️ Cold Lead"

    df['Tier'] = df['TFIDF_Score'].apply(assign_tier)

    # Display results
    st.success("✅ Lead scoring complete!")
    st.dataframe(df[['Name', 'Title', 'Company', 'TFIDF_Score', 'Tier']])

    # Download button
    st.download_button(
        label="📥 Download Scored Leads",
        data=df.to_csv(index=False),
        file_name="scored_leads.csv",
        mime="text/csv"
    )
else:
    st.info("👆 Please upload a CSV file with an 'About' column to begin.")
