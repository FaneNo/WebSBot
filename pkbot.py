import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://pokemondb.net/pokedex/national')

pok = []

content = driver.page_source
# Load the contents of the page, its source, into BeautifulSoup class, which analyzes the HTML and allows to select its elements.
soup = BeautifulSoup(content, 'html.parser')
counter = 0

#It has the filter `attrs` given to it in order to return data that is in that class.
for pokemon_container in soup.find_all(attrs={'class': 'infocard-list'}):
    counter += 1
    if pokemon_container:
        #every a pokemon_container loop that a generation 
        pok.append(f'Generation {counter}')
        
        for pokemon in pokemon_container.find_all('div', class_='infocard'):
            ndex_element = pokemon.find('span', class_='infocard-lg-data text-muted')
            name_element = pokemon.find('span', class_='infocard-lg-data text-muted').find('a', class_='ent-name')
            type_elements = pokemon.find_all('a', class_='itype')
            if ndex_element and name_element:
                ndex = ndex_element.find('small').text.strip()
                name = name_element.text.strip()
                type = [t.text.strip() for t in type_elements]
                pok.append(f'{ndex}: {name} ({", ".join(type)})')
                
    
                
cv = pd.DataFrame({'Pokemon': pok})
cv.to_csv('Pokemon.csv', index=False, encoding='utf-8')

ex = pd.DataFrame({'Pokemon': pok})
ex.to_excel('Pokemon.xlsx', index=False,sheet_name='Sheet_name_1' )


for x in pok:
    print(x)


    