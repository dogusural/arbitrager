import tkinter as tk
from PIL import ImageTk, Image




root = tk.Tk()
root.title("Arbitrager")
root.geometry("500x500")

label = tk.Label(root, fg="dark green")
label1 = tk.Label(root, fg="black",text='Capital',anchor="e",justify='left')
label.pack()
label1.pack()


image_kraken = Image.open("img/kraken.jpg")
image_kraken = image_kraken.resize((64, 64), Image.ANTIALIAS)
img_kraken = ImageTk.PhotoImage(image_kraken)
panel_kraken = tk.Label(root, image = img_kraken)

panel_kraken.pack(side = "left", fill = "both", expand = "yes")


image_paribu = Image.open("img/paribu.png")
image_paribu = image_paribu.resize((64, 64), Image.ANTIALIAS)
img_paribu = ImageTk.PhotoImage(image_paribu)
panel_paribu = tk.Label(root, image = img_paribu)
panel_paribu.pack(side = "right", fill = "both", expand = "yes")


entry = tk.Entry(root)
entry.pack()


def uplabel():
    txt = entry.get()
    label1.config(text=txt)

button = tk.Button(root, text='Stop', width=100, command=root.destroy)
button1 = tk.Button(root, text='Calculate Arbitrage', width=100, command=lambda :uplabel())
button1.pack()

button.pack()
root.mainloop()

