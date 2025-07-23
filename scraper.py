import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrap_url(url, item_type):
    all_data = []
    page = 1

    while True:
        full_url = f"{url}?page={page}"
        response = requests.get(full_url)
        if response.status_code != 200:
            print(f"Erreur de chargement: {full_url}")
            break
        soup = BeautifulSoup(response.text, 'html.parser')
        containers = soup.find_all('div', class_='col s6 m4 l3')

        if not containers:
            break

        for container in containers:
            try:
                prix = container.find('p', class_='ad__card-price').text.replace('CFA', '').strip()
                adresse = container.find('p', class_='ad__card-location').span.text.strip()
                description = container.find('p', class_='ad__card-description').text.strip()
                image = container.find('img', class_='ad__card-img')['src']
                all_data.append({
                    'type': item_type,
                    'description': description,
                    'prix': prix,
                    'adresse': adresse,
                    'image_lien': image
                })
            except:
                continue
        print(f"Page {page} traitée.")
        page += 1
    return pd.DataFrame(all_data)

# URLS à scraper
urls = [
    ('https://sn.coinafrique.com/categorie/vetements-homme', 'habits_homme'),
    ('https://sn.coinafrique.com/categorie/chaussures-homme', 'chaussures_homme'),
    ('https://sn.coinafrique.com/categorie/vetements-enfants', 'habits_enfants'),
    ('https://sn.coinafrique.com/categorie/chaussures-enfants', 'chaussures_enfants')
]

# Récupérer toutes les données
df_total = pd.DataFrame()

for url, item_type in urls:
    df_page = scrap_url(url, item_type)
    df_total = pd.concat([df_total, df_page], ignore_index=True)

# Sauvegarder dans un fichier CSV
df_total.to_csv('donnees_brutes.csv', index=False)
print("Scraping terminé, données enregistrées dans 'donnees_brutes.csv'.")