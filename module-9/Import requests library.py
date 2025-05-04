# Import requests library
import requests

# Put URL for the API in
url = "http://api.open-notify.org/astros.json"

# Make the GET request for the API
response = requests.get(url)

# Check if our request was successful
if response.status_code == 200:
    # JSON response
    data = response.json()
    
    # Print number of astronauts that are currently in space
    print(f"There are {data['number']} astronauts in space right now.\n")

    # Print every astronaut's name
    for person in data['people']:
        print(f"- {person['name']}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
