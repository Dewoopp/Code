import tkinter as Tk

class Image:
    def __init__(self, filename, x, y, root, canvas):
        img = Tk.PhotoImage(filename, master = root)
        self.img = canvas.create_image(x, y, anchor=Tk.NW, image=img)