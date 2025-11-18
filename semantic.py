# ------------------------------------------------------------
# semantic.py
# Analizador Semántico para PHP
# ------------------------------------------------------------

import datetime
import os

# tablas de símbolos
tabla_clases = {}       
tabla_funciones = {}     
errores_semanticos = []  

def registrar_error(msg):
    errores_semanticos.append(msg)

# ------------------------------------------------------------
# INTEGRANTE 1: ANGIE ALFONSO - Comienzo
# ------------------------------------------------------------

def analizar_clase(nombre):
    # verifica si ya existe clase
    if nombre in tabla_clases:
        registrar_error(f"Error semántico: la clase '{nombre}' ya está declarada.")
    else:
        tabla_clases[nombre] = True

def analizar_funcion(nombre):
    # verifica si ya existe función
    if nombre in tabla_funciones:
        registrar_error(f"Error semántico: la función '{nombre}' ya está declarada.")
    else:
        tabla_funciones[nombre] = True

# recorrido del AST
def analizar_nodo(nodo):

    if not isinstance(nodo, tuple):
        return

    tipo = nodo[0]

    if tipo == "clase":
        analizar_clase(nodo[1])

    if tipo == "function_def":
        analizar_funcion(nodo[1])

    # recorrer hijos
    for elem in nodo[1:]:
        if isinstance(elem, list):
            for sub in elem:
                analizar_nodo(sub)
        else:
            analizar_nodo(elem)

# ejecutar semántico
def ejecutar_semantico(ast, usuario):

    tabla_clases.clear()
    tabla_funciones.clear()
    errores_semanticos.clear()

    analizar_nodo(ast)

    fecha = datetime.datetime.now().strftime("%d-%m-%Y-%Hh%M")
    nombre_log = f"semantico-{usuario}-{fecha}.txt"

    os.makedirs("logs", exist_ok=True)

    with open(f"logs/{nombre_log}", "w", encoding="utf-8") as log:
        log.write("Analizador Semántico\n")
        log.write(f"Usuario: {usuario}\n")
        log.write(f"Fecha: {fecha}\n")
        log.write("--------------------------------------------------\n\n")

        if errores_semanticos:
            for err in errores_semanticos:
                log.write(err + "\n")
        else:
            log.write("No se encontraron errores semánticos.\n")

    print(f"Log generado en logs/{nombre_log}")


# ------------------------------------------------------------
# INTEGRANTE 1: ANGIE ALFONSO - Fin
# ------------------------------------------------------------

if __name__ == "__main__":
    from parser import parser

    archivo = "algoritmo1.php"
    usuario = "angie329"

    with open(archivo, "r", encoding="utf-8") as f:
        codigo = f.read()
    ast = parser.parse(codigo)
    ejecutar_semantico(ast, usuario)