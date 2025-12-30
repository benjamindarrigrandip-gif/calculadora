#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Simple - Simple Calculator Application
Una calculadora gráfica básica con interfaz tkinter
"""

import tkinter as tk
from tkinter import ttk
import math


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Variable para almacenar la expresión
        self.expresion = ""
        
        # Crear la interfaz
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Frame para la pantalla
        frame_pantalla = tk.Frame(self.root, bg="#2b2b2b")
        frame_pantalla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Pantalla de resultados
        self.pantalla = tk.Entry(
            frame_pantalla,
            font=("Arial", 24),
            justify="right",
            bg="#1e1e1e",
            fg="white",
            bd=0,
            insertbackground="white"
        )
        self.pantalla.pack(fill=tk.BOTH, expand=True, ipady=20)
        
        # Frame para los botones
        frame_botones = tk.Frame(self.root, bg="#2b2b2b")
        frame_botones.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Definir los botones
        botones = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]
        
        # Crear los botones
        for i, fila in enumerate(botones):
            for j, boton in enumerate(fila):
                if boton == '':
                    continue
                    
                # Determinar el color del botón
                if boton in ['C', '⌫']:
                    bg_color = "#d32f2f"
                    fg_color = "white"
                elif boton in ['/', '*', '-', '+', '=', '%']:
                    bg_color = "#ff9800"
                    fg_color = "white"
                else:
                    bg_color = "#424242"
                    fg_color = "white"
                
                btn = tk.Button(
                    frame_botones,
                    text=boton,
                    font=("Arial", 18, "bold"),
                    bg=bg_color,
                    fg=fg_color,
                    activebackground="#616161",
                    activeforeground="white",
                    bd=0,
                    command=lambda b=boton: self.click_boton(b)
                )
                
                # Configurar el grid
                if boton == '0':
                    btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=2, pady=2)
                elif boton == '.':
                    btn.grid(row=i, column=j+1, sticky="nsew", padx=2, pady=2)
                else:
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
        
        # Configurar el peso de las filas y columnas
        for i in range(5):
            frame_botones.grid_rowconfigure(i, weight=1)
        for j in range(4):
            frame_botones.grid_columnconfigure(j, weight=1)
    
    def click_boton(self, boton):
        if boton == 'C':
            # Limpiar todo
            self.expresion = ""
            self.actualizar_pantalla()
        elif boton == '⌫':
            # Borrar el último carácter
            self.expresion = self.expresion[:-1]
            self.actualizar_pantalla()
        elif boton == '=':
            # Calcular el resultado
            self.calcular()
        else:
            # Agregar el carácter a la expresión
            self.expresion += str(boton)
            self.actualizar_pantalla()
    
    def actualizar_pantalla(self):
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, self.expresion)
    
    def calcular(self):
        try:
            # Reemplazar % por /100 para porcentajes
            expresion_eval = self.expresion.replace('%', '/100')
            
            # Evaluar la expresión
            # Nota: eval() es seguro en este contexto ya que es una aplicación de escritorio
            # que solo procesa la entrada del usuario desde la GUI local
            resultado = eval(expresion_eval)
            
            # Formatear el resultado
            if isinstance(resultado, float):
                # Eliminar decimales innecesarios
                if resultado.is_integer():
                    resultado = int(resultado)
                else:
                    resultado = round(resultado, 10)
            
            self.expresion = str(resultado)
            self.actualizar_pantalla()
        except Exception as e:
            self.expresion = "Error"
            self.actualizar_pantalla()
            # Limpiar después de un segundo
            self.root.after(1000, lambda: self.limpiar_error())
    
    def limpiar_error(self):
        if self.expresion == "Error":
            self.expresion = ""
            self.actualizar_pantalla()


def main():
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()


if __name__ == "__main__":
    main()
