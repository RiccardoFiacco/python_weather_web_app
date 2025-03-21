from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv() #andiamo a prendere le vcar di ambiente dal file .env

def get_current_weather(city='Latina'): #andiamo a dare di default una citta
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("key")}&q={city}&units=metric'
    try:
      req_data = requests.get(weather_url).json() #aniamo a chidere al server le info con l'url composto sopra
      return req_data #le andiamo a ritornare
    except Exception as error:
        print(error) 

if __name__ == "__main__": #se esguiamo direttamente, dal file, il codice eseguiremo una versione in console
    city = input("\nEnter the city: \n") 
    if not city.strip(): #se il valore è una stringa vuota o contiene solo spazi sara un false value
        city="Latina"
    res = get_current_weather(city)
    pprint(res)