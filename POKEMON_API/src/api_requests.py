"""
   Vamos a realizar nuestra primera pericion a una API.
"""
import requests

# La api
api_url = "https://pokeapi.co/api/v2/pokemon/25"
# Peticion
response = requests.get(api_url, timeout = 10)
# Para revisar si hubo error en la peticion
response.raise_for_status()

print(response.status_code) 
pokemons = response.json()

# Tipos de variables de pokemons
print(type(pokemons))

# Pokemons
# print(pokemons)

# Vamos a imprimir id 
print("Id: ", pokemons["id"])
print("Nombre: ", pokemons["name"])
print("No recuerdo:", pokemons["is_default"])
print("altura del pokemon", pokemons["height"]/10)
print("Peso:", pokemons["weigh"]/10)

for element in pokemons["types"]:
    print("Pokemon tipo: ", element["type"]["name"])
