
class Jugada:

    def __init__ (self,numero,jugador,columna):
        self.numero = numero
        self.jugador = jugador
        self.columna = columna

    def __str__(self):
        print ("Jugada",self.numero,"para el jugador", self.jugador, ": Introduce ficha en la columna ", self.columna)