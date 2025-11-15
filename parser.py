# ------------------------------------------------------------
# parser.py
# Analizador Sintáctico para PHP usando PLY - yacc
# ------------------------------------------------------------

import ply.yacc as yacc
from lexer import tokens
import datetime
import os

# ============================================================
# INTEGRANTE 1: ANGIE ALFONSO
# ============================================================

def p_program(p):
    '''program : statement_list'''
    p[0] = ("programa", p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                        | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : assignment
                | print_statement
                | if_statement
                | class_definition
                | php_open
                | php_close'''
    p[0] = p[1]


def p_php_open(p):
    '''php_open : PHP_OPEN'''
    # esto ignora a <?php
    p[0] = ("php_open",)


def p_php_close(p):
    '''php_close : PHP_CLOSE'''
    # esto ignora a ?>
    p[0] = ("php_close",)

# asignación
def p_assignment(p):
    '''assignment : VARIABLE EQUALS expression SEMI'''
    p[0] = ("asignacion", p[1], p[3])

# print (echo)
def p_print_statement(p):
    '''print_statement : ECHO expression SEMI'''
    p[0] = ("print", p[2])

# if/else
def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN block
                    | IF LPAREN expression RPAREN block ELSE block'''
    if len(p) == 6:
        p[0] = ("if", p[3], p[5])
    else:
        p[0] = ("if_else", p[3], p[5], p[7])


# bloques ( {...} )
def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    p[0] = ("bloque", p[2])


# definición de las clases
def p_class_definition(p):
    '''class_definition : CLASS ID LBRACE class_body RBRACE'''
    p[0] = ("clase", p[2], p[4])

def p_class_body(p):
    '''class_body : class_body class_member
                | class_member
                | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    elif p[1] is None:
        p[0] = []
    else:
        p[0] = [p[1]]

def p_class_member(p):
    '''class_member : PUBLIC VARIABLE SEMI
                    | PRIVATE VARIABLE SEMI
                    | PROTECTED VARIABLE SEMI
                    | FUNCTION ID LPAREN RPAREN block'''
    if p[1] in ("public", "private", "protected"):
        p[0] = ("propiedad", p[1], p[2])
    else:
        p[0] = ("metodo", p[2], p[5])


# ============================================================
# INTEGRANTE 2 - rellenar su parte
# ============================================================


# ============================================================
# INTEGRANTE 3 - rellenar su parte
# ============================================================

#poniendo temporalmente la función que le toca al integrante 3 ( completarla mejor ) para que funcione el parser
def p_expression_basic(p):
    '''expression : VARIABLE
                | NUMBER
                | STRING
                | TRUE
                | FALSE'''
    p[0] = ("exp_basica", p[1])



# utilidades

def p_empty(p):
    'empty :'
    pass

#Manejo de errores 
def p_error(p):
    if p:
        synthetic_errors.append(
            f"Error de sintaxis cerca de '{p.value}' en la línea {p.lineno}"
        )
    else:
        synthetic_errors.append("Error de sintaxis inesperado (EOF)")


# Ejecución y Log

synthetic_errors = []
parser = yacc.yacc()

def ejecutar_parser(archivo, usuario):
    global synthetic_errors
    synthetic_errors = []

    if not os.path.exists(archivo):
        print(f"No se encontró {archivo}")
        return

    with open(archivo, "r", encoding="utf-8") as f:
        data = f.read()

    parser.parse(data)

    fecha = datetime.datetime.now().strftime("%d-%m-%Y-%Hh%M")
    logname = f"sintactico-{usuario}-{fecha}.txt"

    os.makedirs("logs", exist_ok=True)

    with open(f"logs/{logname}", "w", encoding="utf-8") as log:
        log.write("Analizador Sintáctico\n")
        log.write(f"Usuario: {usuario}\n")
        log.write(f"Fecha: {fecha}\n")
        log.write("="*50 + "\n\n")

        if synthetic_errors:
            for err in synthetic_errors:
                log.write(err + "\n")
        else:
            log.write("No se encontraron errores sintácticos.\n")

    print(f"Log generado en logs/{logname}")



#prueba 
if __name__ == "__main__":
    ejecutar_parser("algoritmo1.php", "angie329")
