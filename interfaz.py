# Angie Alfonso - Comienzo

import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import os

import lexer
import parser
import semantic

# Funciones de la interfaz

def cargar_archivo():
    ruta = filedialog.askopenfilename(
        filetypes=[("Archivos PHP", "*.php"), ("Todos", "*.*")]
    )
    if ruta:
        with open(ruta, "r", encoding="utf-8") as f:
            codigo = f.read()
        entrada_texto.delete("1.0", tk.END)
        entrada_texto.insert(tk.END, codigo)
        global archivo_actual
        archivo_actual = ruta


def ejecutar_lexico():
    contenido = entrada_texto.get("1.0", tk.END)
    if not contenido.strip():
        messagebox.showwarning("Advertencia", "No hay código para analizar.")
        return
    
    lexer.lexer.input(contenido)

    salida_texto.delete("1.0", tk.END)
    salida_texto.insert(tk.END, "=== Análisis Léxico ===\n\n")

    while True:
        tok = lexer.lexer.token()
        if not tok:
            break
        salida_texto.insert(tk.END, f"{tok.type}\t{tok.value}\tLínea {tok.lineno}\n")


def ejecutar_sintactico():
    contenido = entrada_texto.get("1.0", tk.END)
    if not contenido.strip():
        messagebox.showwarning("Advertencia", "No hay código para analizar.")
        return

    salida_texto.delete("1.0", tk.END)
    salida_texto.insert(tk.END, "=== Análisis Sintáctico ===\n\n")

    parser.synthetic_errors.clear()
    parser.parser.parse(contenido)

    if parser.synthetic_errors:
        for err in parser.synthetic_errors:
            salida_texto.insert(tk.END, err + "\n")
    else:
        salida_texto.insert(tk.END, "No se encontraron errores sintácticos.\n")


def ejecutar_semantico():
    contenido = entrada_texto.get("1.0", tk.END)
    if not contenido.strip():
        messagebox.showwarning("Advertencia", "No hay código para analizar.")
        return

    salida_texto.delete("1.0", tk.END)
    salida_texto.insert(tk.END, "=== Análisis Semántico ===\n\n")

    semantic.errores_semanticos.clear()
    semantic.ejecutar_semantico(contenido, "usuario_gui")

    if semantic.errores_semanticos:
        for err in semantic.errores_semanticos:
            salida_texto.insert(tk.END, err + "\n")
    else:
        salida_texto.insert(tk.END, "No se encontraron errores semánticos.\n")


# INTERFAZ

ventana = tk.Tk()
ventana.title("Analizador Léxico – Sintáctico – Semántico (PHP)")
ventana.geometry("1000x650")
ventana.configure(bg="#f2f2f2")

archivo_actual = None

#Entrada 
tk.Label(ventana, text="Código PHP:", bg="#f2f2f2", font=("Segoe UI", 12, "bold")).pack()

entrada_texto = scrolledtext.ScrolledText(ventana, width=110, height=15, font=("Consolas", 11))
entrada_texto.pack(pady=5)

# Botones
frame_botones = tk.Frame(ventana, bg="#f2f2f2")
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Cargar Archivo", command=cargar_archivo, width=15).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Léxico", command=ejecutar_lexico, width=10, bg="#d9e6ff").grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Sintáctico", command=ejecutar_sintactico, width=10, bg="#d9ffd9").grid(row=0, column=2, padx=5)
tk.Button(frame_botones, text="Semántico", command=ejecutar_semantico, width=10, bg="#ffe6e6").grid(row=0, column=3, padx=5)

# Salida
tk.Label(ventana, text="Resultados:", bg="#f2f2f2", font=("Segoe UI", 12, "bold")).pack()

salida_texto = scrolledtext.ScrolledText(ventana, width=110, height=15, font=("Consolas", 11), fg="#333")
salida_texto.pack(pady=5)

ventana.mainloop()

# Angie Alfonso - Fin