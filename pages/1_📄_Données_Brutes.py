import streamlit as st
import pandas as pd

st.title("📄 Données Brutes (Web Scraper)")

uploaded_file = st.sidebar.file_uploader("✨ Téléchargez un fichier brut (.csv)", type=["csv"])
if uploaded_file:
    df_raw = pd.read_csv(uploaded_file)
    st.success("✅ Données brutes chargées avec succès")
    st.dataframe(df_raw)
else:
    st.info("📂 Aucun fichier importé.")
