import requests 
import sys
def weather():
    print("Hello! The bot has started")
    city = input("Kindly give your location in the format city,(state)->")

    if not city:
        print("Kindly rewrite the city you want")
        return
    headers = {'User-Agent':'Project/2025'}

    print("Bot is fetching your location")
    geo_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
   
    geo_response= requests.get(geo_url,headers=headers)
    geo_data = geo_response.json()
    if not geo_data:
           print("Invalid location")
           return

    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]
    weather_location = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,precipitation"
    weather_response = requests.get(weather_location)
    print("Location found\nFinding weather just wait for a few seconds")
    weather_data = weather_response.json()
    if "current" in weather_data:
     temp = weather_data["current"]["temperature_2m"]
     rain = weather_data["current"]["precipitation"]
     humidity = weather_data["current"]["relative_humidity_2m"]

     aqi_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&current=us_aqi"
     aqi_response = requests.get(aqi_url)
     aqi_data = aqi_response.json()
     if "current" in aqi_data:
      aqi = aqi_data["current"]["us_aqi"]
      print("===WEATHER REPORT===")
      print(f" 📍 Location->{city}")
      print(f" 🌡  Temperature->{temp}")
      print(f" 💧 Humidity->{humidity}")
      print(f" 🌧  Rain chance->{rain}%")
      print(f" 😷 Air Quality->{aqi}")
      print("====Precautions====")
      if aqi > 250:
         print("Its better to not go outside🟥🟥🟥")
      if 250>aqi>150:
         print("Its better to go outside wearing mask🟧🟧🟧")
      if 150> aqi > 100:
         print("its okay quality🟨🟨🟨")
      if 99>aqi>0:
         print("The air quality is good🟩🟩🟩 ,you should go somehere out🏞🏞🏞")
      if humidity >= 70:
         print("Don't wash your clothes❌❌❌")
      elif 70>=humidity>=40:
         print("It's okay if you wash your clothes today✅")
      elif 40>humidity:
         print("It's an good day to wash your clothes✅✅✅")        
     
     
      if temp<0 or temp>10:
        print("The temperature is in negative it will be better if you dont go outside ❄")
      elif 10<=temp<=20:
        print("The temperature is cold, wear some hot clothes and you can go outside🌨")
      elif 35>=temp > 20:
        print("The temperature is okay, you should get outside♨")
      elif temp>35:
         print("There is hot outside you should avoid going out🔥")
      if 100>=rain>=90:
         print("There is very much chances of rain,you should avoid going outside⛈⛈⛈")
      if 90>rain>=70:
         print("There is high possibility of rain🌧🌧🌧 .Go outside either via rain coat or umbrella☔☔☔")
      if 70>rain>=40:
         print("There is good possibility of rain🌦🌦🌦 ,Try to go with umbrella☂☂☂")
      if 40>rain:
         print("There are slight chances of rain 🌦🌦 , but you can go outside with no worries🌂 ")
   
if __name__ =="__main__":
 weather()
input("\nPress Enter to exit...")
