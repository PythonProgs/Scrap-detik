import requests
from bs4 import BeautifulSoup

html_doc = requests.get('http://www.detik.com/terpopuler', params={'tag_from':'wp_cb_mostPopular_more'})
soup = BeautifulSoup(html_doc.text, 'html.parser')

popular_area = soup.findAll(attrs={'class':'media__title'})
images = soup.findAll(attrs={'class':'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])