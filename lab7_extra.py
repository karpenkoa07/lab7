import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def kitty_photo():
    try:
        resp = requests.get("https://nekos.best/api/v2/neko", timeout=5)
        url = resp.json()["results"][0]["url"]
        img = Image.open(BytesIO(requests.get(url).content))
        img = img.resize((400, 400))
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo
    except:
        label.config(text="Error ^^")

root = tk.Tk()
label = tk.Label(root)
label.pack()
btn = tk.Button(root, text="Press for a new picture ^^", command=kitty_photo)
btn.pack()
kitty_photo()
root.mainloop()
