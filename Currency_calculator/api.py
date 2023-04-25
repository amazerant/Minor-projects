#functions written by Mazerant Adam https://github.com/amazerant

import requests, json, csv, re


res = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/?format=json")

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4, ensure_ascii=False)
    return text

table = jprint(res.json())

kody = []
waluty = []
mid = []

print('New table of exchange rates was downloaded')

pattern1 = re.compile(r'"code": "\w{3}"')
matches1 = pattern1.findall(table)

pattern2 = re.compile(r'"currency": "[^\n]+"')
matches2 = pattern2.findall(table)

pattern3 = re.compile(r'"mid": \d\.\d+')
matches3 = pattern3.findall(table)


for match in matches1:
    kody.append(match.replace('"code": ',''))
    
for match in matches2:
    waluty.append(match.replace('"currency": ',''))

for match in matches3:
    mid.append(match.replace('"mid": ',''))

with open('exchange.csv', mode='w') as plik:
    plik = csv.writer(plik, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(len(mid)):
        plik.writerow([kody[i], waluty[i], mid[i]])



