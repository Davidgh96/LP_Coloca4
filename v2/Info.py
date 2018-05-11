from tkinter import *
from tkinter import font

class Info(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=1000, height=800)
        police = font.Font(self, size=20, family='Arial', weight="bold")
        self.t = Label(self, text="Jugador 1 [amarillo]", font=police)
        self.t.grid(sticky=NSEW, pady=20)