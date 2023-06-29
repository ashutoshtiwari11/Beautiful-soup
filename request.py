import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import cv2 as cv
import numpy

id=input('enter Id of pokemon e.g. bulbasaur === 1 ')
url = "https://pokemon.gameinfo.io/en/pokemon/" + id

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

elements = soup.find_all('div', class_='type')
typ = []  # types of the pokemon

name_element = soup.find('h1', class_='')
pokemon_name = name_element.text.strip()

for element in elements:
    typ.append(element.text)

mainmove = soup.find('select', class_='mainmove')
main_moves = mainmove.text

description = soup.find('p', class_='info')
pokemon_description = description.text

weakness = soup.find('table', class_="weaknesses")
rows = weakness.find_all('td')

weaknesses = []

for weak in rows:
    weaknesses.append(weak.text.strip())

resis = soup.find('table', class_="weaknesses res")
rows = resis.find_all('td')

resistances = []
for weak in rows:
    resistances.append(weak.text.strip())

evolutions = soup.find('article', class_='evolution-block')
evolution_title = evolutions.find('h2').text.strip()
evolution_details = evolutions.text.strip()

# Writing all the data to 'notes.txt' file
with open('notes.txt', 'w', encoding='utf-8') as file:
    file.write(f"Pokemon Name: {pokemon_name}\n\n")
    file.write(f"Types: {', '.join(typ)}\n\n")
    file.write(f"Main Moves: {main_moves}\n\n")
    file.write(f"Description: {pokemon_description}\n\n")
    file.write("Weak Against:\n")
    for weakness in weaknesses:
        file.write(f"- {weakness}\n")
    file.write("\nResistance Against:\n")
    for resistance in resistances:
        file.write(f"- {resistance}\n")
    file.write(f"\n{evolution_title}\n{evolution_details}\n")

img_tag = soup.find('img')
img = requests.get(img_tag['src'])
image = Image.open(BytesIO(img.content))
path=pokemon_name+'.png'
image.save(path)

