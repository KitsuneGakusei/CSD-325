# pokeapi_program.py

import requests

# URL for a specific Pokémon
url = 'https://pokeapi.co/api/v2/pokemon/sylveon'

# Make the GET request
response = requests.get(url)

# Step 1: Test the connection
print("Status Code:", response.status_code)

# Step 2: Print the raw, unformatted response
print("\nRaw JSON Output:")
print(response.text)

# Step 3: Print the formatted, clean output
if response.status_code == 200:
    data = response.json()
    
    print("\nFormatted Output:")
    print(f"Name: {data['name'].capitalize()}")
    print(f"ID: {data['id']}")
    print("Abilities:")
    for ability in data['abilities']:
        print(f"- {ability['ability']['name']}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
