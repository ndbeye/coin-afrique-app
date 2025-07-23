import pandas as pd

# Charger le fichier brut
df = pd.read_csv('donnees_brutes.csv')

# Nettoyer le prix : enlever espaces, 'CFA', convertir en number si nécessaire
df['prix'] = df['prix'].apply(lambda x: ''.join(filter(str.isdigit, str(x))))

# Nettoyer adresse (exemple simple)
df['adresse'] = df['adresse'].str.strip()

# Vérifier et ajuster l’url de l'image
df['image_lien'] = df['image_lien'].apply(lambda x: x if x.startswith('http') else 'https://sn.coinafrique.com' + x)

# Enregistrer les données nettoyées
df.to_csv('donnees_netoyees.csv', index=False)
print("Nettoyage terminé, fichier 'donnees_netoyees.csv' prêt.")