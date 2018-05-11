import tkinter
from tkinter import *
from tkinter import font
from tkinter import messagebox

from espacioVacio import *
from espacioVacioMenu import *
from Info import *

from Ficha import *





class Tablero(Canvas):
    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=600, height=500, bg="blue")

        self.valores = []

        self.jugador = 1
        self.color = "yellow"
        self.tabla = []
        self.perm = True
        self.puntos1=0
        self.puntos2=0
        self.cont=0
        self.turn=1

        for i in range(6):
            self.valores.append([])
            for j in range(7):
                self.valores[i].append("white")
        i=0
        j=0

        for i in range(10, 440, int(500 / 6)):
            lista_rango = []
            for j in range(10, 540, int(600 / 7)):
                lista_rango.append(Ficha(j, i, self))

            self.tabla.append(lista_rango)

        self.bind("<Button-1>", self.detCol)

    def vaciarTablero(self):
        global  textoTurno
        self.turn=1
        textoTurno.set("Turno " + str(self.turn))
        for i in range(0, 6):
            for j in range(0, 7):
                self.tabla[i][j].changeColor("white")
                self.valores[i][j]="white"

    def detCol(self, event):
        global textoTurno
        if self.perm:
            col = int(event.x / 85)
            fila = 0
            if (self.tabla[0][col].color == 'red' or self.tabla[0][col].color == 'yellow'):
                tkinter.messagebox.showwarning('Error', 'Columna llena. \n Elige otra por favor.')
            else:
                while fila < len(self.tabla):

                    if self.tabla[0][col].color == "red" or self.tabla[0][0].color == "yellow":
                        break

                    if self.tabla[fila][col].color == "red" or self.tabla[fila][col].color == "yellow":
                        self.tabla[fila - 1][col].changeColor(self.color)
                        self.valores[fila - 1][col]= self.color
                        break

                    elif fila == len(self.tabla) - 1:
                        self.tabla[fila][col].changeColor(self.color)
                        self.valores[fila][col]=self.color
                        break

                    if self.tabla[fila][col].color != "red" and self.tabla[fila][col].color != "yellow":
                        fila += 1

                if self.jugador == 1:
                    self.jugador = 2
                    info.t.config(text="Jugador 2 [rojo]")
                    self.color = "red"

                elif self.jugador == 2:
                    self.jugador = 1
                    info.t.config(text="Jugador 1 [amarillo]")
                    self.color = "yellow"

                self.Horizontal()
                self.Vertical()
                self.Diagonal1()
                self.Diagonal2()

                if(self.cont == 0):
                    self.cont += 1
                else:
                    self.cont = 0
                    self.turn += 1
                    textoTurno.set("Turno " + str(self.turn))


                if ((self.tabla[0][0].color == 'red' or self.tabla[0][0].color == 'yellow') and
                        (self.tabla[0][1].color == 'red' or self.tabla[0][1].color == 'yellow') and
                        (self.tabla[0][2].color == 'red' or self.tabla[0][2].color == 'yellow') and
                        (self.tabla[0][3].color == 'red' or self.tabla[0][3].color == 'yellow') and
                        (self.tabla[0][4].color == 'red' or self.tabla[0][4].color == 'yellow') and
                        (self.tabla[0][5].color == 'red' or self.tabla[0][5].color == 'yellow') and
                        (self.tabla[0][6].color == 'red' or self.tabla[0][6].color == 'yellow')):
                    respuesta = tkinter.messagebox.askyesno('FIN', 'Nadie ha ganado. \n\n¿Jugar otra partida?.')
                    if respuesta == True:
                        #reiniciar()
                        self.vaciarTablero()
                    else:
                        VentanaJuego.destroy()

    def Horizontal(self):
        global  textoPuntos,menu
        i = 0
        while (i < len(self.tabla)):
            j = 0
            while (j < 4):
                if self.tabla[i][j].color == self.tabla[i][j + 1].color == self.tabla[i][j + 2].color == self.tabla[i][
                    j + 3].color == "red":
                    info.t.config(text="¡Victoria del rojo!")

                    if(self.turn>4):
                        self.puntos2 += 50 - (2*self.turn)
                    else:
                        self.puntos2 += 50

                    textoPuntos.set('Jugador 1: \n\n' + str(self.puntos1) +
                             ' puntos\n\nJugador 2:\n\n' + str(self.puntos2) + ' puntos')

                    respuesta = tkinter.messagebox.askyesno('FIN', 'Ha ganado el jugador 2\n\nEl jugador 2 tiene '+
                                                            str(self.puntos2)+' puntos \n\n¿Jugar otra partida?.')
                    if respuesta == True:

                        self.vaciarTablero()
                        self.turn=0
                        info.t.config(text="Jugador 1 [amarillo]")
                        self.color="yellow"
                        self.jugador=1
                    else:
                        VentanaJuego.destroy()
                        menu=1

                    #self.perm = False
                    break
                elif (self.tabla[i][j].color == self.tabla[i][j + 1].color == self.tabla[i][j + 2].color == self.tabla[i][
                    j + 3].color == "yellow"):
                    info.t.config(text="¡Victoria del amarillo!")

                    if (self.turn > 4):
                        self.puntos1 += 50 - (2*self.turn)
                    else:
                        self.puntos1 += 50

                    textoPuntos.set('Jugador 1: \n\n' + str(self.puntos1) +
                             ' puntos\n\nJugador 2:\n\n' + str(self.puntos2) + ' puntos')

                    respuesta = tkinter.messagebox.askyesno('FIN', 'Ha ganado el jugador 1\n\nEl jugador 1 tiene '+
                                                            str(self.puntos1)+' puntos \n\n¿Jugar otra partida?.')
                    if respuesta == True:

                        self.vaciarTablero()
                        self.turn = 0
                        info.t.config(text="Jugador 1 [amarillo]")
                        self.color = "yellow"
                        self.jugador = 1
                    else:
                        VentanaJuego.destroy()
                        menu=1

                    #self.perm = False
                    break
                j += 1
            i += 1

    def Vertical(self):
        global textoPuntos,menu
        i = 0
        while (i < 3):
            j = 0
            while (j < len(self.tabla[i])):
                if (self.tabla[i][j].color == self.tabla[i + 1][j].color == self.tabla[i + 2][j].color == self.tabla[i + 3][
                    j].color == "red"):
                    info.t.config(text="¡Victoria del rojo!")

                    if(self.turn>4):
                        self.puntos2 += 50 - (2*self.turn)
                    else:
                        self.puntos2 += 50

                    textoPuntos.set('Jugador 1: \n\n' + str(self.puntos1) +
                             ' puntos\n\nJugador 2:\n\n' + str(self.puntos2) + ' puntos')

                    respuesta = tkinter.messagebox.askyesno('FIN', 'Ha ganado el jugador 2\n\nEl jugador 2 tiene '+
                                                            str(self.puntos2)+' puntos \n\n¿Jugar otra partida?.')
                    if respuesta == True:

                        self.vaciarTablero()
                        self.turn=0
                        info.t.config(text="Jugador 1 [amarillo]")
                        self.color = "yellow"
                        self.jugador = 1
                    else:
                        VentanaJuego.destroy()
                        menu=1

                    #self.perm = False
                    break
                elif (self.tabla[i][j].color == self.tabla[i + 1][j].color == self.tabla[i + 2][j].color == self.tabla[i + 3][
                    j].color == "yellow"):
                    info.t.config(text="¡Victoria del amarillo!")

                    if (self.turn > 4):
                        self.puntos1 += 50 - (2*self.turn)
                    else:
                        self.puntos1 += 50

                    textoPuntos.set('Jugador 1: \n\n' + str(self.puntos1) +
                             ' puntos\n\nJugador 2:\n\n' + str(self.puntos2) + ' puntos')

                    respuesta = tkinter.messagebox.askyesno('FIN', 'Ha ganado el jugador 1\n\nEl jugador 1 tiene '+
                                                            str(self.puntos1)+' puntos \n\n¿Jugar otra partida?.')
                    if respuesta == True:

                        self.vaciarTablero()
                        turn = 0
                        info.t.config(text="Jugador 1 [amarillo]")
                        self.color = "yellow"
                        self.jugador = 1
                    else:
                        VentanaJuego.destroy()
                        menu=1

                    break
                j += 1
            i += 1

    def Diagonal1(self):
        global textoPuntos, menu
        i = 0
        while (i < 3):
            j = 0
            while (j < 4):
                if (self.tabla[i][j].color == self.tabla[i + 1][j + 1].color == self.tabla[i + 2][j + 2].color == self.tabla[i + 3][
                    j + 3].color == "red"):
                    info.t.config(text="¡Victoria del rojo!")

                    if(self.turn>4):
                        self.puntos2 += 50 - (2*self.turn)
                    else:
                        self.puntos2 += 50

                    textoPuntos.set('Jugador 1: \n\n' + str(self.puntos1) +
                             ' puntos\n\nJugador 2:\n\n' + str(self.puntos2) + ' puntos')

                    respuesta = tkinter.messagebox.askyesno('FIN', 'Ha ganado el jugador 2\n\nEl jugador 2 tiene '+
                                                            str(self.puntos2)+' puntos \n\n¿Jugar otra partida?.')
                    if respuesta == True:

                        self.vaciarTablero()
                        self.turn=0
                        info.t.config(text="Jugador 1 [amarillo]")
                        self.color = "yellow"
                        self.jugador = 1
                    else:
                        VentanaJuego.destroy()
                        menu=1

                    #self.perm = False
                    break
                elif (self.tabla[i][j].color == self.tabla[i + 1][j + 1].color == self.tabla[i + 2][j + 2].color == self.tabla[i + 3][
                    j + 3].color == "yellow"):
                    info.t.config(text="¡Victoria del amarillo!")


                    if (self.turn > 4):
                        self.puntos1 += 50 - (2*self.turn)
                    else:
                        self.puntos1 += 50

                    textoPuntos.set('Jugador 1: \n\n' + str(self.puntos1) +
                             ' puntos\n\nJugador 2:\n\n' + str(self.puntos2) + ' puntos')

                    respuesta = tkinter.messagebox.askyesno('FIN', 'Ha ganado el jugador 1\n\nEl jugador 1 tiene '+
                                                            str(self.puntos1)+' puntos \n\n¿Jugar otra partida?.')
                    if respuesta == True:

                        self.vaciarTablero()
                        self.turn = 0
                        info.t.config(text="Jugador 1 [amarillo]")
                        self.color = "yellow"
                        self.jugador = 1
                    else:
                        VentanaJuego.destroy()
                        menu=1

                    break
                j += 1
            i += 1

    def Diagonal2(self):
        global  textoPuntos, menu
        i = 0
        while (i < 3):
            j = len(self.tabla[i]) - 1
            while (j > len(self.tabla) - 4):
                if (self.tabla[i][j].color == self.tabla[i + 1][j - 1].color == self.tabla[i + 2][j - 2].color == self.tabla[i + 3][
                    j - 3].color == "red"):
                    info.t.config(text="¡Victoria del rojo!")

                    if(self.turn>4):
                        self.puntos2 += 50 - (2*self.turn)
                    else:
                        self.puntos2 += 50

                    textoPuntos.set('Jugador 1: \n\n' + str(self.puntos1) +
                             ' puntos\n\nJugador 2:\n\n' + str(self.puntos2) + ' puntos')

                    respuesta = tkinter.messagebox.askyesno('FIN', 'Ha ganado el jugador 2\n\nEl jugador 2 tiene '+
                                                            str(self.puntos2)+' puntos \n\n¿Jugar otra partida?.')
                    if respuesta == True:

                        self.vaciarTablero()
                        self.turn=0
                        info.t.config(text="Jugador 1 [amarillo]")
                        self.color = "yellow"
                        self.jugador = 1
                    else:
                        VentanaJuego.destroy()
                        menu=1

                    #self.perm = False
                    break
                elif (self.tabla[i][j].color == self.tabla[i + 1][j - 1].color == self.tabla[i + 2][j - 2].color == self.tabla[i + 3][
                    j - 3].color == "yellow"):
                    info.t.config(text="¡Victoria del amarillo!")

                    if (self.turn > 4):
                        self.puntos1 += 50 - (2*self.turn)
                    else:
                        self.puntos1 += 50

                    textoPuntos.set('Jugador 1: \n\n' + str(self.puntos1) +
                             ' puntos\n\nJugador 2:\n\n' + str(self.puntos2) + ' puntos')

                    respuesta = tkinter.messagebox.askyesno('FIN', 'Ha ganado el jugador 1\n\nEl jugador 1 tiene '+
                                                            str(self.puntos1)+' puntos \n\n¿Jugar otra partida?.')
                    if respuesta is True:

                        self.vaciarTablero()
                        self.turn = 0
                        info.t.config(text="Jugador 1 [amarillo]")
                        self.color = "yellow"
                        self.jugador = 1
                    else:
                        VentanaJuego.destroy()
                        menu=1

                    break
                j -= 1
            i += 1

    def getValores(self):
        return self.valores

    def getJugador(self):
        return self.jugador

    def getColor(self):
        return self.color

    def getTurno(self):
        return self.turn

    def getPuntos1(self):
        return self.puntos1

    def getPuntos2(self):
        return self.puntos2

    def setValores(self, valores):
        self.valores=valores
        for i in range(0, 6):
            for j in range(0, 7):
                self.tabla[i][j].changeColor(self.valores[i][j])

    def setJugador(self,jugador):
        self.jugador=int(jugador)

    def setColor(self,color):
        self.color=color

    def setTurno(self,turno):
        self.turn=int(turno)

    def setPuntos1(self,puntos1):
        self.puntos1=int(puntos1)

    def setPuntos2(self,puntos2):
        self.puntos2=int(puntos2)

#----------------------------------------------------------------------------------------------------------------------
tipoPartida = "nada"
salir = 0
menu = 1

tmpJugador = 1
tmpColor = "white"
tmpTurno = 0
tmpPuntos1 = 0
tmpPuntos2 = 0
tmpValores = []

for i in range(6):
    tmpValores.append([])
    for j in range(7):
        tmpValores[i].append("white")
#----------------------------------------------------------------------------------------------------------------------
"""
def reiniciar():
    global info
    info.t.config(text="")

    info = Info(root)
    info.grid(row=0, column=1)

    p = espacioVacio(root)
    p.grid(row=1, column=0)
    p2 = espacioVacio(root)
    p2.grid(row=2, column=0)
    p3 = espacioVacio(root)
    p3.grid(row=0, column=0)

    t = Terrain(root)
    t.grid(row=1, column=1)
"""


def guardarFichero():
    global VentanaJuego
    try:
        file = open("ultima_partida.txt", "w")
        valores = t.getValores()
        jugador = t.getJugador()
        color = t.getColor()
        turno = t.getTurno()
        puntos1 = t.getPuntos1()
        puntos2 = t.getPuntos2()
        file.write(str(jugador) + '\n')
        file.write(color + '\n')
        file.write(str(turno) + '\n')
        file.write(str(puntos1) + '\n')
        file.write(str(puntos2) + '\n')
        for i in range(0, 6):
            for j in range(0, 7):
                file.write(valores[i][j] + '\n')
    finally:
        file.close()
        VentanaJuego.destroy()


def leerFichero():
    global menu,salir,tablero,\
        tmpValores,tmpPuntos2,tmpPuntos1,tmpTurno,tmpJugador, tmpColor, tipoPartida
    valores = []
    for i in range(6):
        valores.append([])
        for j in range(7):
            valores[i].append("white")
    file = open("ultima_partida.txt","r")
    jugador = file.readline()
    color = file.readline()
    if (color == "white\n"):
        color = color[:5]
    elif (color == "red\n"):
        color = color[:3]
    else:
        color = color[:6]
    turno = file.readline()
    puntos1 = file.readline()
    puntos2 = file.readline()
    for i in range(0, 6):
        for j in range(0, 7):
            valores[i][j]=file.readline()
            if(valores[i][j]=="white\n"):
                valores[i][j]=valores[i][j][:5]
                tmpValores[i][j]=valores[i][j]
            elif(valores[i][j]=="red\n"):
                valores[i][j] = valores[i][j][:3]
                tmpValores[i][j] = valores[i][j]
            else:
                valores[i][j] = valores[i][j][:6]
                tmpValores[i][j] = valores[i][j]
    tmpColor=color
    tmpJugador=int(jugador)
    tmpTurno=int(turno)
    tmpPuntos1=int(puntos1)
    tmpPuntos2=int(puntos2)
    tipoPartida = "fichero"
    salir=1

    file.close()
    ventanaMenu.destroy()



def salirJuego():
    global salir,menu
    salir=0
    menu=0
    ventanaMenu.destroy()


def Instrucciones():
    tkinter.messagebox.showinfo('Instrucciones',
    'Como jugar: \n\n-Cada jugador deberá intentar alinear 4 fichas diagonal,horizontal o verticalmente. \n\n'
    '-Para colocar una ficha se debe hacer click en la columna deseada y la ficha se colocará lo más abajo posible.\n\n'
    '-La puntuación perfecta es 100 puntos solo posible para los jugadores que ganen en 4 turnos, desde ahí se restarán '
    'dos puntos por cada turno de cada jugador. \n\n-Sólo el jugador que gane conseguirá puntos')


def jugar():
    global tipoPartida, salir
    tipoPartida = "jugar"
    salir=1
    ventanaMenu.destroy()


def Cerrar():
    global salir
    salir=0
    VentanaJuego.destroy()

#Menu-------------------------------------------------------------------------------------------------------------------
"""
Creamos el menu con las 4 opciones
"""
while (menu == 1):
    try:
        ventanaMenu = Tk()
        ventanaMenu.geometry("1000x800")
        ventanaMenu.title("menu")
        police = font.Font(ventanaMenu, size=30, family='Arial', weight='bold')
        botones = font.Font(ventanaMenu, size=20, family='Arial')
        m = Menu(ventanaMenu)
        p = espacioVacioMenu(ventanaMenu)
        p.grid(row=0, column=0)
        p0 = espacioVacioMenu(ventanaMenu)
        p0.grid(row=0, column=0)
        p1 = Label(ventanaMenu, bg="blue", height=3, width=15,
                   relief=RAISED, text='4 EN LÍNEA',
                   pady=10, fg="white", font=police)
        p1.grid(row=1, column=1)
        Button(ventanaMenu, text="Jugar", command=jugar, bd=6, width=14, height=1, font=botones, bg="#d3d3d3")\
            .grid(row=2, column=1, pady=10)
        Button(ventanaMenu, text="Partida guardada", command=leerFichero, bd=6, width=14, height=1, font=botones,
               bg="#d3d3d3").grid(row=3, column=1, pady=10)
        Button(ventanaMenu, text="Salir", command=salirJuego, bd=6, width=14, height=1, font=botones, bg="#d3d3d3") \
            .grid(row=5, column=1, pady=10)
        Button(ventanaMenu, text="Instrucciones", command=Instrucciones, bd=6, width=14, height=1, font=botones,
               bg="#d3d3d3").grid(row=4, column=1, pady=10)
        ventanaMenu.mainloop()
    finally:
        menu=0

    while (salir == 1):#creamos la ventana del juego
        VentanaJuego = Tk()
        VentanaJuego.geometry("1000x800")
        VentanaJuego.title("4 en línea")
        p = espacioVacio(VentanaJuego)
        p.grid(row=1, column=0)
        p2 = espacioVacio(VentanaJuego)
        p2.grid(row=2, column=0)
        p3 = espacioVacio(VentanaJuego)
        p3.grid(row=0, column=0)
        btn = font.Font(VentanaJuego, size=15, family='Arial')
        # Button(root, text="Reiniciar", command=reiniciar).grid(row=2, column=1, pady=30)
        Button(VentanaJuego, text="Guardar y salir", command=guardarFichero, bd=6, width=14, height=1, font=btn,
               bg="#d3d3d3").grid(row=2, column=1, pady=10)
        Button(VentanaJuego, text="Volver al menú", command=Cerrar, bd=6, width=14, height=1, font=btn, bg="#d3d3d3") \
            .grid(row=3, column=1, pady=10)

        trn = font.Font(VentanaJuego, size=40, family='Arial', weight='bold')

        if (tipoPartida== "fichero"):
            try:

                t = Tablero(VentanaJuego)
                t.grid(row=1, column=1)
                t.setJugador(tmpJugador)
                t.setColor(tmpColor)
                t.setTurno(tmpTurno)
                t.setPuntos1(tmpPuntos1)
                t.setPuntos2(tmpPuntos2)
                t.setValores(tmpValores)

                text = tmpColor
                if (tmpColor == "red"):
                    text = "rojo"
                else:
                    text = "amarillo"

                info = Info(VentanaJuego)
                info.grid(row=0, column=1)
                info.t.config(text="Jugador" + str(tmpJugador) + "[" + text + "]")

                textoTurno = StringVar()
                Label(VentanaJuego, textvariable=textoTurno, font=trn, padx=10, bg="#d3d3d3").grid(row=0, column=2)
                textoTurno.set("Turno " + str(tmpTurno))

                textoPuntos = StringVar()
                Label(VentanaJuego, textvariable=textoPuntos, padx=10, bg="#d3d3d3").grid(row=1, column=2)
                textoPuntos.set("Jugador 1: \n" + str(tmpPuntos1) + " puntos \n\nJugador 2: \n" +
                                str(tmpPuntos2) + " puntos")

                VentanaJuego.mainloop()
            finally:
                salir = 0
                menu = 1
        if tipoPartida == "jugar":
            try:

                info = Info(VentanaJuego)
                info.grid(row=0, column=1)

                t = Tablero(VentanaJuego)
                t.grid(row=1, column=1)

                textoTurno = StringVar()
                Label(VentanaJuego, textvariable=textoTurno, font=trn, padx=10, bg="#d3d3d3").grid(row=0, column=2)
                textoTurno.set("Turno 1")

                textoPuntos = StringVar()
                Label(VentanaJuego, textvariable=textoPuntos, padx=10, bg="#d3d3d3").grid(row=1, column=2)
                textoPuntos.set("Jugador 1: \n0 \npuntos \n\nJugador 2: \n0 \npuntos")

                VentanaJuego.mainloop()
            finally:
                salir = 0
                menu = 1





