#ACTIVIDAD -2. Pandas

import pandas as pd
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import plotly.express as px

def abrir():  
    """Función que abre el fichero y lo asigna a una variable global."""
    global df
    filename = filedialog.askopenfilename(parent=root, initialdir = "./dat/", title = "Selecciona archivo",
                                    filetypes = (("csv","*.csv"),("all files","*.*")))
    nombre.set(filename)
    df=pd.read_csv(filename, sep=";")
    #display(df)

def calcular():
    """Función que calcula Dataframe a utilizar, según lo marcado por el usuario. E imprime por pantalla los datos. """
    global dfcalc
    operaciones=[]
    columnas=[]
    texto.delete(1.0, END)
    if opcion1.get()==1:
        columnas.insert(0, 'centro')
    elif opcion1.get()==2:
        columnas.insert(0, 'tipo')
    elif opcion1.get()==3:
        columnas.insert(0, 'c_postal')
    if opcion2.get()==1:
        columnas.append('mes')
    elif opcion2.get()==2:
        columnas.append('anyy')
    if factura.get()==1:
        operaciones.append('count')
    if ventas.get()==1:
        operaciones.append('sum') 
    if len(operaciones) > 0 :
        dfcalc=df.groupby(columnas).agg({'total_fra': operaciones})
        texto.insert('insert', dfcalc)     
    else :
        texto.insert('insert', 'No ha seleccionado operaciones.')

def lineas():
    """Distintas funciones a imprimir dependiendo de la opción. """
    dfcalc.plot()
    plt.show()
   
def barras():
    dfcalc.plot(kind='bar')
    plt.show()
    
def tartas():
    fig = px.pie(df, values='total_fra', names='mes')
    fig.show()
   
    
        
root = Tk()
root.title("Actividad 2")

nombre=StringVar()
opcion1=IntVar()
opcion2=IntVar()
factura=IntVar()
ventas=IntVar()
grafico=IntVar()

Entry(root,textvariable=nombre,state=DISABLED,width=60).grid(row = 0,column = 0)
Button(root,text="Navega",command=abrir).grid(row = 0,column = 1)

Label(root ,text = "Agrupar por").grid(row = 2,column = 0)
Radiobutton(root, text="Centro", variable=opcion1, value=1).grid(row = 2,column = 1)
Radiobutton(root, text="Tipo de Cliente", variable=opcion1, value=2).grid(row = 2,column =2)
Radiobutton(root, text="Distrito", variable=opcion1, value=3).grid(row = 2,column = 3)

Label(root ,text = "Desglose").grid(row = 4,column = 0)
Radiobutton(root, text="Por meses", variable=opcion2, value=1).grid(row = 4,column = 1)
Radiobutton(root, text="Total anual", variable=opcion2, value=2).grid(row = 4,column = 2)

Checkbutton(root, text="Nº de factura", variable=factura, onvalue=1, offvalue=0).grid(row = 5,column = 1)
Checkbutton(root, text="Total ventas", variable=ventas, onvalue=1, offvalue=0).grid(row = 5,column = 2)

Label(root ,text = "Resultado:").grid(row = 6,column = 0)
Button(root,text="Calcular",command=calcular).grid(row = 6,column = 3)

texto = Text(root)
texto.grid(row=7, columnspan=10)
texto.config(padx=5, pady=4, bd=0, font=("Consolas", 12))

Label(root,text = "Gráfico").grid(row =8,column=0)
Button(root,text="Líneas",command=lineas).grid(row = 8,column = 1)
Button(root,text="Barras",command=barras).grid(row = 8,column = 2)
Button(root,text="Tartas",command=tartas).grid(row = 8,column = 3)

root.mainloop()