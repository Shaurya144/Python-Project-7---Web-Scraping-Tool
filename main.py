import requests
from bs4 import BeautifulSoup

url = "https://scrapeme.live/shop/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

ul_elements = soup.find('ul', class_="products columns-4")
li_elements = ul_elements.find_all('li')

for li in li_elements:
    title = li.find('h2', class_="woocommerce-loop-product__title").text
    price = li.find('span', class_="price").text
    url = li.find('a', class_="woocommerce-LoopProduct-link woocommerce-loop-product__link")['href']

    pokemon = {
        "title": title,
        "price": price,
        "url": url
    }

    print(pokemon)