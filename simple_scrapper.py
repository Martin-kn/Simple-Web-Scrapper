from bs4 import BeautifulSoup
import requests


html_text = requests.get(
        'https://www.cyberciti.biz/'
).text

soup = BeautifulSoup(html_text, 'lxml')

links = soup.find_all(href=True, rel=True)

print("""
Recent Entries:
""")

for link in links:
  if soup.find(rel=True) and bool(link.text):
    title = link.text
    extra = soup.find('div', class_ = "post_content").text
    post_link = link['href']
    
    print(f'\nTitle: {title}\n {extra}\nLink: {post_link}\n')

