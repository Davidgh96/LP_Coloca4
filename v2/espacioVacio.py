import tkinter
from tkinter import *

class espacioVacio(Canvas):
    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=150, height=10)