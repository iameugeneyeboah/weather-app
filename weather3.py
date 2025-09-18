from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")

import requests
r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=London&APPID={API_KEY}')
pprint(r.json())

