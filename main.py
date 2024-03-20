import requests
from tkinter import *

# Main window
root = Tk()
root.minsize(300, 300)
root.resizable(False, False)
root.title("Aplikace na urážky")


response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
response.raise_for_status()
data = response.json()

print(data["insult"])
