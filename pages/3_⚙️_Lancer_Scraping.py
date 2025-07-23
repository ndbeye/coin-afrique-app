import streamlit as st
import os

st.title("⚙️ Scraping Manuel des Données")

if st.button("🚀 Lancer le Scraping maintenant"):
    with st.spinner("Scraping en cours..."):
        os.system("python scraper.py")
        os.system("python nettoyage.py")
        st.success("✅ Scraping et nettoyage terminés !")
