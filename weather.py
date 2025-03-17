from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv() #andiamo a prendere le vcar di ambiente dal file .env

def get_current_weather(city="Latina"): #andimao a dare di default una citta
    print(city)