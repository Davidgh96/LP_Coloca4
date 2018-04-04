class Tablero:

    def __init__(self):
        self.tablero = []
        for i in range(6):
            self.tablero.append(['.'] * 7)

    def insertarFicha(self,columna,jugador):
        fila= self.posicionEnColumna(columna)
        if jugador==1:
            self.tablero[fila][columna-1]='x'
        else:
            self.tablero[fila][columna-1]='o'
        return fila

    def esColumnaLLena(self,columna):
        return self.tablero[0][columna-1]!='.'

    def esTableroLLeno(self):
        return self.tablero[0][0] != '.' and self.tablero[0][1] != '.' and self.tablero[0][2] != '.' and self.tablero[0][3] != '.' and self.tablero[0][4] != '.' and self.tablero[0][5] != '.' and self.tablero[0][6] != '.'

    def esVictoria(self):
        fila=6
        columna=7
        victoria=False
        for i in range(0,fila):
            for j in range(0,columna):
                if j+3<columna and self.comprobarFila(i,j):
                    victoria=True
                if i+3< fila and self.comprobarColumna(i,j):
                    victoria=True
                if i+3<fila and j+3<columna and self.comprobarDiagonalDerecha(i,j):
                    victoria=True
                if i+3<fila and j-3>-1 and self.comprobarDiagonalIzquierda(i,j):
                    victoria=True

        return victoria

    def comprobarFila(self,i,j):
        return self.tablero[i][j]==self.tablero[i][j+1]==self.tablero[i][j+2]==self.tablero[i][j+3]!='.'

    def comprobarColumna(self,i,j):
        return self.tablero[i][j]==self.tablero[i+1][j]==self.tablero[i+2][j]==self.tablero[i+3][j]!='.'
    def comprobarDiagonalDerecha(self,i,j):

        return self.tablero[i][j] == self.tablero[i+1][j + 1] == self.tablero[i+2][j + 2] == self.tablero[i+3][j + 3] != '.'

    def comprobarDiagonalIzquierda(self, i, j):
        return self.tablero[i][j] == self.tablero[i + 1][j - 1] == self.tablero[i + 2][j - 2] == self.tablero[i + 3][j - 3] != '.'

    def posicionEnColumna(self,pos):
        encontrado=-1
        actual=5
        while(actual>=0 and encontrado==-1):
            if (self.tablero[actual][pos-1]=='.'):
                encontrado=actual
            actual=actual-1
        return encontrado

    def __str__(self):
        for i in range(0,6):
            for j in range(0,7):
                print(self.tablero[i][j],end=' ')
            print()

tablero=Tablero()


contador=0
while(tablero.esVictoria()==False and tablero.esTableroLLeno()==False):
    jugador= (contador % 2) +1
    print("Turno Jugador ",jugador)
    c=int(input("Elija una columna no vacia"))
    while(tablero.esColumnaLLena(c)):
        c = int(input("Elija una columna no vacia"))
    tablero.insertarFicha(c,jugador)
    tablero.__str__()
    if tablero.esVictoria():
        print("El Jugador ",jugador," ha ganado!")
    elif tablero.esTableroLLeno():
        print("Habeis empatado")
    contador=contador+1
