import streamlit as st

st.set_page_config(page_title="Accueil - CoinAfrique", page_icon="🏠", layout="wide")

st.title("🏠Dashboard CoinAfrique")
st.markdown("""
Bienvenue dans votre application de scraping et d’analyse de données **CoinAfrique** 📊

**Fonctionnalités disponibles :**
- 📄 Voir les données brutes téléchargées depuis Web Scraper
- 🔍 Explorer les données nettoyées
- ⚙️ Lancer manuellement le scraping
- 💬 Donner votre avis

Utilisez le **menu à gauche** pour naviguer entre les pages.
""")

st.image("https://cdn-icons-png.flaticon.com/512/4208/4208443.png", width=150)
