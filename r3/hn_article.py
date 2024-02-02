import requests
import json

# Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.
# URL = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
URL = "https://hacker-news.firebaseio.com/v0/item/39231096.json"
r = requests.get(URL)
print(f"Kod statusu: {r.status_code}")

# Analiza struktur danych.
response_dict = r.json()
readable_file = 'data/readable_hn_data3.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
