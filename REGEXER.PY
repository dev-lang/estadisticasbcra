''' Data Scraper para estadísticas BCRA '''
''' (c) 2022 github.com/dev-lang '''

import re
import requests

archivo = "lista.txt"
invalid = "/////"
baseurl = "https://api.estadisticasbcra.com/"
auth = ""
api_url = list()

with open(archivo) as f:
    for l in f.readlines():
        if not invalid in l:
            regex = re.search(r"(com)(\/)([\w+]{3,})", l)
            apicode = regex.group(3)
        pass
        api_url.append(apicode)

print(api_url)

def DataScraper(i):
    response = requests.get(str(baseurl+api_url[i]), headers={'Authorization': auth})
    json_response = response.json()
    print(api_url[i])
    archivo = api_url[i] + ".json"
    with open(archivo, 'w') as jout:
        jout.write(str(json_response))
    return json_response

#for i in range(0,2):
for i in range(len(api_url)):
    DataScraper(i)
