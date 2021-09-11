from bs4 import BeautifulSoup
import requests


html_text = requests.get(
        'https://www.cyberciti.biz/'
).text

soup = BeautifulSoup(html_text, 'lxml')

links = soup.find_all(href=True, rel=True)

print("""
Entradas Recientes:
""")

for link in links:
  if soup.find(rel=True) and bool(link.text):
    print(link.text)
    if link.has_attr('href'):
      print(link['href'], "\n")

