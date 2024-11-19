import json
import requests
request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()

        joke = json_response["value"]
        print(joke)
    else:
        print(f"Error: Received status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")