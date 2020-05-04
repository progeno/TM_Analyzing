#import requests

#r = requests.get("https://ssimeonoff.github.io/cards-list")
#print(r.text)


import requests
from bs4 import BeautifulSoup
url = 'https://ssimeonoff.github.io/cards-list'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html5lib")
print("1")
# pierwszym argumentem konstruktora klasy BeautifulSoup jest zawartośc dokumentu HTML
# drugim parametrem jest parser i nad nim się chwilę zatrzymamy