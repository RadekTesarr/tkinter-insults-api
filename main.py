import requests
from tkinter import *

# Main window
root = Tk()
root.minsize(300, 300)
root.resizable(False, False)
root.title("Aplikace na urážky")
root.config(bg="#042940")


# Functions
def insult_me():
    user_language = drop_down_lang.get()
    param = {
        "lang": user_language,
        "type": "json"
    }

    response = requests.get("https://evilinsult.com/generate_insult.php", params=param)
    response.raise_for_status()
    data = response.json()
    insult_label.config(text=data["insult"])


# Roller shutter - language
drop_down_lang = StringVar(root)
drop_down_lang.set("cs")
drop_down_lang_options = OptionMenu(root, drop_down_lang, "cs", "en", "pl", "es", "fr")
drop_down_lang_options.config(bg="#005C35", fg="white", font=("Arial", 12))
drop_down_lang_options.pack(pady=10)

# Button
insult_button = Button(text="Chci urazit", command=insult_me, bg="#005C53", fg="white", font=("Arial", 12))
insult_button.pack(pady=10)

# Label
insult_label = Label(wraplength=250, bg="#042940", fg="#D6D58E", font=("Arial", 14))
insult_label.pack()

# Mainloop
root.mainloop()
