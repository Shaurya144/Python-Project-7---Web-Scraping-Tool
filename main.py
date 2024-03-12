from pprint import pprint
import requests
from bs4 import BeautifulSoup
url = "https://scrapeme.live/shop/"

def scrape_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def pokemon_list(soup):
    ul_elements = soup.find('ul', class_="products columns-4")
    return ul_elements.find_all('li')

def scrape_pokemon(li):
    name = li.find('h2', class_="woocommerce-loop-product__title").text
    price = li.find('span', class_="price").text
    url = li.find('a', class_="woocommerce-LoopProduct-link woocommerce-loop-product__link")['href']
    pokemon = {
        "name": name,
        "price": price,
        "url": url
    }
    return pokemon

pokemons = []
pages = 1

for page in range(0, pages):
    print(page)
    url = "https://scrapeme.live/shop/page/%d" % page

    soup = scrape_page(url)
    li_elements = pokemon_list(soup)

    
    for li in li_elements:
        pokemon = scrape_pokemon(li)
        pokemons.append(pokemon)


for i in range(0 , len(pokemons)):
    pokemon = pokemons[i]
    url = pokemon['url']
    soup = scrape_page(url)

    stock = soup.find('p', class_="stock in-stock").text

    pokemon['stock'] = stock
    print(url)



pprint(pokemons) # Use pprint to make your prints look good

# This gives you the price, Name and stock of each pokemon
