# ------------------------------------------------------------
# semantic.py
# Analizador Semántico para PHP
# ------------------------------------------------------------

import datetime
import os

try:
    from parser import parser
    from lexer import lexer
except ImportError:
    print("Error: Asegúrate de que parser.py y lexer.py estén en el mismo directorio.")
    exit(1)


# --- Almacenamiento Global de Errores ---
errores_semanticos = [] 
def registrar_error(msg):
    errores_semanticos.append(msg)

# ============================================================
# INTEGRANTE 1: ANGIE ALFONSO - Lógica de Clases y Funciones
# ============================================================

# Tablas globales solo para clases y funciones (definidas globalmente)
tabla_clases = {} 
tabla_funciones = {} 

def analizar_clase(nombre, linea=0):
    # verifica si ya existe clase
    if nombre in tabla_clases:
        registrar_error(f"Error Semántico (Línea {linea}): la clase '{nombre}' ya está declarada.")
    else:
        tabla_clases[nombre] = True
        print(f"Clase registrada: {nombre}")

def analizar_funcion(nombre, linea=0):
    # verifica si ya existe función
    if nombre in tabla_funciones:
        registrar_error(f"Error Semántico (Línea {linea}): la función '{nombre}' ya está declarada.")
    else:
        # Miembro 3 debería expandir esto para guardar parámetros
        tabla_funciones[nombre] = {'params': 0} 
        print(f"Función registrada: {nombre}")

# ============================================================
# INTEGRANTE 2: Cykes07
# ============================================================

class SymbolTable:
    """ Maneja los ámbitos (scopes) de las variables """
    def __init__(self):
        self.scopes = [{}]
        print("SymbolTable (Variables) inicializada.")

    def enter_scope(self):
        self.scopes.append({})
        print(f"Entrando a scope de variable (Nivel {len(self.scopes)})")

    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()
            print(f"Saliendo de scope (Nivel {len(self.scopes)})")

    def add_variable(self, name, line=0):
        current_scope = self.scopes[-1]
        if name not in current_scope:
            current_scope[name] = True
            print(f"Variable registrada: {name} en scope {len(self.scopes)}")

    def lookup_variable(self, name, line=0):
        encontrado = False
        for scope in reversed(self.scopes):
            if name in scope:
                encontrado = True
                break
        
        if not encontrado:
            registrar_error(f"Error Semántico (Línea {line}): Variable '{name}' usada pero no declarada.")
        
        return encontrado



def analizar_nodo(nodo, symbol_table):

    if not isinstance(nodo, tuple):
        return

    tipo = nodo[0]
    
    if tipo == "clase":
        analizar_clase(nodo[1]) 
        symbol_table.enter_scope()
        analizar_nodo(nodo[2], symbol_table) 
        symbol_table.exit_scope() 
        return 

    if tipo == "function_def":
        analizar_funcion(nodo[1]) 
        symbol_table.enter_scope() 
        analizar_nodo(nodo[2], symbol_table) 
        symbol_table.exit_scope() 
        return

    if tipo == "asignacion":
        var_name = nodo[1]
        
        analizar_nodo(nodo[2], symbol_table)
        
        symbol_table.add_variable(var_name)
        return 

    if tipo == "variable":
        var_name = nodo[1]
        symbol_table.lookup_variable(var_name)
        return 

    for elem in nodo[1:]:
        if isinstance(elem, list):
            for sub_nodo in elem:
                analizar_nodo(sub_nodo, symbol_table)
        else:
            analizar_nodo(elem, symbol_table)


def ejecutar_semantico(codigo_php, usuario):
    
    tabla_clases.clear()
    tabla_funciones.clear()
    errores_semanticos.clear()
    
    var_symbol_table = SymbolTable()
    
    print("Iniciando análisis sintáctico...")
    ast = parser.parse(codigo_php, lexer=lexer.clone(), tracking=True)
    if not ast:
        print("Error grave de sintaxis, no se puede continuar con el análisis semántico.")
        registrar_error("Error Sintáctico Crítico: No se pudo generar el AST.")

    if ast and not errores_semanticos:
        print("Iniciando análisis semántico...")
        analizar_nodo(ast, var_symbol_table)
    

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



if __name__ == "__main__":

    

    archivo = "algoritmo_semantico.php"
    usuario = "Cykes07" 

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            codigo = f.read()
        
        # Ejecutar el análisis
        ejecutar_semantico(codigo, usuario)
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de prueba '{archivo}'.")