import requests
import json

response = requests.get("https://wolnelektury.pl/api/books/")

print(response.status_code)  # HTTP status (e.g., 200)
res = response.json()

all = {
    "epoch": {}
}


counter = 0

for book in res:
    print(book['title'])  # Print the title of each book
    print(book['slug'])
    txt = "https://wolnelektury.pl/media/book/txt/" + book['slug'] + ".txt"
    print(txt)
    counter += 1

    # if counter > 100:
    #     break

    check_txt = requests.get(txt)
    if check_txt.status_code == 200:
        if book['epoch'] not in all['epoch']:
            all['epoch'][book['epoch']] = {}
        if book['slug'] not in all['epoch'][book['epoch']]:
            all['epoch'][book['epoch']][book['slug']] = {}
        all['epoch'][book['epoch']][book['slug']]['url'] = book['url']
        all['epoch'][book['epoch']][book['slug']]['title'] = book['title']
        all['epoch'][book['epoch']][book['slug']]['slug'] = book['slug']
        all['epoch'][book['epoch']][book['slug']]['author'] = book['author']
        all['epoch'][book['epoch']][book['slug']]['genre'] = book['genre']
        all['epoch'][book['epoch']][book['slug']]['txt'] = txt
      # Print the title of each book
print(json.dumps(all, indent=4, ensure_ascii=False))

with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(all, f, ensure_ascii=False, indent=4)

with open('books.csv', 'w', encoding='utf-8') as f:
    f.write("epoch,title,slug,author,genre,url,txt\n")
    for epoch, data in all['epoch'].items():
        for slug, book in data.items():
            f.write(f"{epoch},{book['title']},{book['slug']},{book['author']},{book['genre']},{book['url']},{book['txt']}\n")