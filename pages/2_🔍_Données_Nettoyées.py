import streamlit as st
import pandas as pd

st.title("🔍 Données Nettoyées Prêtes à l’Analyse")

try:
    df = pd.read_csv("donnees_netoyees.csv")
    st.success("✅ Données nettoyées chargées.")
    st.dataframe(df)
except:
    st.error("⚠️ Fichier `donnees_netoyees.csv` introuvable.")
