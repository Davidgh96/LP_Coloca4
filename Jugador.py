
from Jugada import Jugada
from Partida import Partida
from Ficha import Ficha

class Jugador:

    def __init__(self, numero):
        self.numero = numero
        self.turno = 0
        self.fichas = [Ficha]
        self.cogerFichas()
        self.jugadas = [Jugada]
        self.fichasDisponibles = 21



    def cogerFichas (self):
        for i in range (0, 21):
            ficha = Ficha (self.numero)
            self.fichas.append (ficha)

    def getNumero (self,numero):
        numero = self.numero

    def usarFicha (self):
        for i in self.fichas:
            if (not i.usada) & (self.fichasDisponibles >0):
                i.usarFicha()
                self.fichasDisponibles = self.fichasDisponibles-1

            else:
                print ("El jugador ", self.numero, " no tiene más fichas y no puede jugar")

        return self.fichas[i.getSimbolo()]

