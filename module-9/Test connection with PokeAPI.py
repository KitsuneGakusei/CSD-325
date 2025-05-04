# Test connection with PokeAPI
import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/sylveon')
print(response.status_code)
*