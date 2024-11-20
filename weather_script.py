import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        weather_description = weather['description']
        
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_description}")
    else:
        print("City not found or API request failed.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "ac076e60f70a1ba264c3939da4a6c24f"  # Replace with your actual API key
    get_weather(city_name, api_key)