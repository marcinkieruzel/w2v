import requests
import json
import os


with open('books.json', 'r', encoding='utf-8') as f:
    all = json.load(f)

for epoch, data in all['epoch'].items():
    if len(data) > 100:
        print(f"Epoch: {epoch} {len(data)} books")
        dir = f"WOLNE_LEKTURY_SCRAPING/books/{epoch}"
        
        os.makedirs(dir, exist_ok=True)
        for slug, book in data.items():
            dir_genres = f"WOLNE_LEKTURY_SCRAPING/genres/{book['genre']}"
            os.makedirs(dir_genres, exist_ok=True)
            print(f"Downloading {book['title']}...")
            txt_url = book['txt']
            response = requests.get(txt_url)
            if response.status_code == 200:
                with open(f"{dir}/{slug}.txt", 'w', encoding='utf-8') as f:
                    f.write(response.text)
                with open(f"{dir_genres}/{slug}.txt", 'w', encoding='utf-8') as f:
                    f.write(response.text)
            else:
                print(f"Failed to download {book['title']} from {txt_url}")