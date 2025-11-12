# CONNECT TO API

# 60. One way to connect to API

# we need the requests library to make api call
# request library we need to install

import requests

base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon_info(name):
    url = f'{base_url}/pokemon/{name}'
    response = requests.get(url) # return response object
    
    if response.status_code == 200:
        pokemon_data = response.json() # convert to python dictionary
        return pokemon_data
    else:
        print(f'Failed to retrieve data {response.status_code}')

pokemon_name = 'pikachu'
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")