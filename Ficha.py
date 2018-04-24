
class Ficha:

    def __init__(self,jugador):
        self.jugadorPropietario = jugador
        self.usada = False
        if self.jugadorPropietario == 1:
            self.simbolo = "x"
        else:
            if self.jugadorPropietario ==2:
                self.simbolo = "o"
            else:
                self.simbolo = "o"

    def usarFicha (self):
        self.usada = true


    def getSimbolo (self):
        return self.simbolo

    def __str__(self):
        print (self.simbolo)
