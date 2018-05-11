
class Ficha(object):
    def __init__(self, x, y, can, color="white", bg="red"):
        self.can = can
        self.x = x
        self.y = y
        self.color = color

        self.tour = 1

        self.r = 30
        self.ficha = self.can.create_oval(self.x + 10, self.y + 10, self.x + 61, self.y + 61, fill=color, outline="blue")

    def changeColor(self, color):
        self.can.itemconfigure(self.ficha, fill=color)
        self.color = color
