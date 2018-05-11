from tkinter import *

class espacioVacioMenu(Canvas):
    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=340, height=150)