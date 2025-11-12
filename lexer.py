# ------------------------------------------------------------
# lexer.php.py
# Analizador léxico para PHP utilizando PLY
# Integrante 1: Angie Alfonso - Comienzo
# ------------------------------------------------------------

import ply.lex as lex
import datetime
import os

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'echo': 'ECHO',
    'class': 'CLASS',
    'new': 'NEW',
    'public': 'PUBLIC',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'true': 'TRUE',
    'false': 'FALSE',
    'null': 'NULL'
}

# Lista de nombres de Tokens

tokens = [
    'PHP_OPEN',
    'PHP_CLOSE',
    'PHP_SHORT_OPEN',
    'COMMENT',
    'BLOCK_COMMENT',
    'ID',
] + list(reserved.values()) #usé list en vez de tuple porque se añadirán más tokens por los otros compañeros

# Expresiones regulares simples
t_PHP_OPEN = r'<\?php'
t_PHP_CLOSE = r'\?>'
t_PHP_SHORT_OPEN = r'<\?='


# Reglas de comentarios

def t_COMMENT(t):
    r'(//[^\n]*|\#[^\n]*)'
    pass

def t_BLOCK_COMMENT(t):
    r'/\*[\s\S]*?\*/'
    pass 

# Identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Contador de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y tabs
t_ignore = ' \t'


# Manejo de errores
def t_error(t):
    print(f"Caracter no reconocido: {t.value[0]}")
    t.lexer.skip(1)


# Construcción del lexer
lexer = lex.lex()


# Función para ejecutar y registrar los resultados
def ejecutar_lexer(nombre_archivo, usuario_git):
    """
    Ejecuta el analizador léxico sobre el archivo PHP especificado
    y genera un log con los tokens reconocidos.
    """
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        data = f.read()

    lexer.input(data)

    # Crear nombre del archivo log
    fecha_hora = datetime.datetime.now().strftime("%d-%m-%Y-%Hh%M")
    nombre_log = f"lexico-{usuario_git}-{fecha_hora}.txt"

    os.makedirs("logs", exist_ok=True)
    with open(f"logs/{nombre_log}", 'w', encoding='utf-8') as log:
        log.write(f"Analizador Léxico PHP - Usuario: {usuario_git}\n")
        log.write(f"Fecha y hora: {fecha_hora}\n")
        log.write("="*50 + "\n\n")

        while True:
            tok = lexer.token()
            if not tok:
                break
            log.write(f"{tok.type}\t{tok.value}\tLínea {tok.lineno}\n")

    print(f"Log generado: logs/{nombre_log}")

# ------------------------------------------------------------
# Integrante 1: Angie Alfonso - Fin
# ------------------------------------------------------------

if __name__ == "__main__":
    prueba = "algoritmo1.php"
    usuario = "angie329"
    if not os.path.exists(prueba):
        print(f"No existe {prueba} — crea ese archivo en la misma carpeta e intenta de nuevo.")
    else:
        ejecutar_lexer(prueba, usuario)