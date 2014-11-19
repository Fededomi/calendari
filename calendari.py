#!/usr/bin/env python
# -*- coding: utf8 -*-

"""Se importan los módulos que serán necesarios para el programa."""

import Tkinter as tk
import calendar
import time


#Creamos una clase nueva que nos servirá para trabajar con los meses

class Fecha():
    """En esta clase trabajamos con meses. Se definen una serie de métodos como
    el de imprimirmes, sumarmes o restarmes"""

    """Con CALENDARI definimos un calendario en el que el primer día de la
    semana sea el lunes. Eso se indica con la opción "0" """
    calendari = calendar.Calendar(0)

    """Se definen una serie de constantes con el módulo time que me sirven para
    determinar la fecha en la que se ejecuta el programa cada vez"""

    anyo = time.localtime()[0]
    mes = time.localtime()[1]
    dia = time.localtime()[2]

    """ Con DIAMES definimos una constante que contendrá una lista con las
    semanas del mes. Esa lista a su vez estará formada por otras listas de
    siete elementos que correponden a los días de la semana."""

    mes_pantalla = calendari.monthdayscalendar(anyo, mes)

    def __init__(self, parent):
        self.parent = parent

    def imprimirmes(self):

        anyoactual = tk.Label(self.parent, text=self.anyo)
        anyoactual.grid(row=0, column=4)

        nombremes = {0:"Enero", 1:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo",
                   6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre",
                   10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

        etiquetames = tk.Label(self.parent, text=nombremes[self.mes])
        etiquetames.grid(row=0, column=3)

        """Con este método se imprime el mes recorriendo la variable DIAMES.
        Se reserva la primera fila del widget para escribir el nombre de los
        días de la semana. Para ello definimos un diccionario con sus nombre"""

        diassemana = {0:"Lunes", 1:"Martes", 2:"Miércoles", 3:"Jueves",
                    4:"Viernes", 5:"Sábado", 6:"Domingo"}
        columna = 0

        for i in diassemana:

            diasemana = tk.Label(self.parent, text=diassemana[i],
                    fg="red" if(diassemana[i] == "Sábado" or diassemana[i] ==
                    "Domingo") else "black")
            diasemana.grid(row=1, column=columna)
            columna += 1


        filasemana = 2

        for i in self.mes_pantalla:

            columna = 0
            for j in i:
                day = tk.Label(self.parent, text=j)
                day.grid(row=filasemana, column=columna)
                columna += 1

            filasemana += 1

    def sumarmes(self):
        """Con este método anyadimos un mes al calendario"""
        if self.mes == 12:
            self.mes = 0
            self.anyo += 1
        else:
            self.mes += 1

    def restarmes(self):
        """Con este método restamos un mes al calendario"""
        if self.mes == 0:
            self.mes = 12
            self.anyo -= 1
        else:
            self.mes -= 1


def main():

    root = tk.Tk()
    root.geometry("800x600")
    root.title("IES")
    prova = Fecha(root)

    prova.sumarmes()
    prova.sumarmes()
    prova.imprimirmes()

    root.mainloop()

if __name__ == main():
    main()
