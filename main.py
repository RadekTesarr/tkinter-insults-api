import requests
from tkinter import *

# Main window
root = Tk()
root.minsize(300, 300)
root.resizable(False, False)
root.title("Aplikace na urážky")

# Roller shutter - language
drop_down_lang = StringVar(root)
drop_down_lang.set("cs")
drop_down_lang_options = OptionMenu(root, drop_down_lang, "en", "cs", "pl", "es", "fr")
drop_down_lang_options.pack()

response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
response.raise_for_status()
data = response.json()
