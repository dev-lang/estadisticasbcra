''' Data Scraper para estadísticas BCRA '''
''' (c) 2022 github.com/dev-lang '''

from bs4 import BeautifulSoup as bs
import requests

url = "https://estadisticasbcra.com/api/documentacion"
response = requests.get(url)

data = response.text
soup = bs(data,'html.parser')
#CODES DENTRO DE LI/UL
filtered = [a for a in (td.find('code') for td in soup.findAll('li')) if a]
scrapedtags = list()

def verListaFiltrada(f):
    print("Lista de filtrada: \n", f)
    
def scrapTags(f):
    for t in f:
        #EVITAR ELEMENTOS REPETIDOS
        if t.get_text(strip=True) not in scrapedtags:
            scrapedtags.append(t.get_text(strip=True))
        pass
        
def verListaScraped(st):
    print("Lista de enlaces: \n", st, "\nCantidad de elementos: ", len(st))
    
def scrapArchivo():
    with open("test.txt", "w") as f:
        for e in scrapedtags:
            f.write(e + "\n")

#verListaFiltrada(filtered)

