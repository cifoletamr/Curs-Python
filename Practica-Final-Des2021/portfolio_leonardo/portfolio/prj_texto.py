# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 20:10:21 2021
Autor: Leonardo da silva

"""

from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
from tkinter import ttk
import pandas as pd
import IPython.core.display


def Navegar():
    global filename
    filename = filedialog.askopenfile()
    
def btn_calcular():
    fich = open("./dat/python.txt", "r", encoding="UTF-8")
    cadena = fich.read()
    cadena = cadena.lower()
    cadena = cadena.replace(".", " ")
    cadena = cadena.replace(",", "")
    fich.close()


    fich = open("./dat/descartar.dat", "r", encoding="UTF-8")
    descartar = fich.read()
    descartar = descartar.split("\n")
    descartar.remove("")
    fich.close()

    palabras = cadena.split(" ") 
    palasin = [x for x in palabras if len(x) > 3 and x not in descartar]
    c = set(palasin)      
    difers = list(c)              
    
    contenido = ""
    contenido += f"Total Palabras: {len(palasin)}\nDiferentes: {len(difers)}\n"
    contenido += "Mapa de conceptos: \n"
    veces = {}
    for p in palasin:
        count = veces.get(p,0)
        veces[p] = count + 1
    claves = veces.keys()
    for p in claves:
        if veces[p] > 2 :
            contenido += "{:15} {}\n".format(p, veces[p])
             
    resultado.insert('insert', contenido)
    
    
# Configuración de la raíz
root = Tk()
root.geometry('900x600')
root.title("Analisis de texto")
texto = Text(root)
texto.pack()
texto.config(width=80, height=10, font=("Consolas",12))
texto.grid(row=1)
navega = ttk.Button(root, text="Navegar", command=Navegar)
navega.grid(row=2, column=1)
Label(root, text="Palabras a Descartar").grid(row=2, column=0)
Label(root, text="Descartar palabras de menos de: ").grid(row=3, column=0)
Entry(root).grid(row=3, column=1)
resultado = Text(root)
resultado.grid()
resultado.config(width=80, height=12, font=("Consolas",12))
resultado.grid(row=4)
calcular = ttk.Button(root, text="Calcular", command=btn_calcular)
calcular.grid(row=5, column=0)

# Finalmente bucle de la aplicación
root.mainloop()