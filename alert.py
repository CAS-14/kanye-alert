import tkinter as tk
from PIL import Image, ImageTk
from random import randint

root = tk.Tk()
root.title("Kanye Alert")

img = Image.open(f"img/{randint(1,10)}.jpg")
hpercent = (200/float(img.size[1]))
wsize = int((float(img.size[0])*float(hpercent)))
img = img.resize((wsize,200), Image.ANTIALIAS)

img = ImageTk.PhotoImage(img)
imglb = tk.Label(image=img)
imglb.image = img

#style = tk.ttk.Style()
#style.configure('W.TButton')
close = tk.Button(root, text="  Ok  ", command=root.destroy)

# Position image
imglb.pack(padx=10,pady=10)
close.pack(padx=10, pady=(0,10))
root.mainloop()