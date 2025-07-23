import streamlit as st

st.title("💬 Donnez votre avis")

with st.form("form_avis"):
    nom = st.text_input("👤 Votre prénom ou pseudo")
    avis = st.text_area("📝 Que pensez-vous de cette application ?")
    submit = st.form_submit_button("✅ Envoyer")

    if submit:
        if nom and avis:
            st.success(f"Merci pour votre retour, {nom} ! 🎉")
            # Optionnel : enregistrer dans un fichier CSV ici
        else:
            st.warning("Merci de remplir tous les champs.")
