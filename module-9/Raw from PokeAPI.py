# Raw output from the PokeAPI
import requests

url = 'https://pokeapi.co/api/v2/pokemon/sylveon'
response = requests.get(url)

# Print the raw JSON text
print(response.text)
