#1
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

#2
import requests
def print_report(city):
    coordinates = return_city_name(city)
    lat = coordinates[0]
    lon = coordinates[1]
    request = (f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=82de97288a8db05cffb3f0e3a74a7d44')
    response = requests.get(request).json()
    weather = response['weather'][0]['main']
    temperature = response['main']['temp']
    print(f'The weather of {city.title()} is {weather} and the temperature is {temperature} °C.')

def return_city_name(city_name):
    name = []
    request = (f"http://api.openweathermap.org/geo/1.0/direct?q={city_name.title()}&appid=82de97288a8db05cffb3f0e3a74a7d44")
    response = requests.get(request).json()
    name.append(response[0]['lat'])
    name.append(response[0]['lon'])
    return name

def main():
    try:
        city_name = input('Enter city name: ')
        print_report(city_name)
    except IndexError:
        print("Invalid city name, please try again.")
        main()

if __name__ == "__main__":
    main()