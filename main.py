import requests
from tkinter import *

response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
response.raise_for_status()
data = response.json()

print(data["insult"])
