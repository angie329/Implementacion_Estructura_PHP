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
    '''statement : expression_statement
                | print_statement
                | if_statement
                | class_definition
                | php_open
                | php_close
                | while_statement
                | function_definition
                | for_statement
                | return_statement'''
    p[0] = p[1]

def p_expression_statement(p):
    '''expression_statement : expression SEMI'''
    p[0] = p[1]

def p_php_open(p):
    '''php_open : PHP_OPEN'''
    # esto ignora a <?php
    p[0] = ("php_open",)


def p_php_close(p):
    '''php_close : PHP_CLOSE'''
    # esto ignora a ?>
    p[0] = ("php_close",)

# expression
def p_expression_assignment(p):
    '''expression : VARIABLE EQUALS expression'''
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
                    | PUBLIC FUNCTION ID LPAREN parameter_list RPAREN block
                    | PRIVATE FUNCTION ID LPAREN parameter_list RPAREN block
                    | PROTECTED FUNCTION ID LPAREN parameter_list RPAREN block
                    | FUNCTION ID LPAREN parameter_list RPAREN block'''
    if p[1] in ("public", "private", "protected"):
        p[0] = ("propiedad", p[1], p[2])
    else:
        p[0] = ("metodo", p[2], p[5])


# ============================================================
# INTEGRANTE 2 - Sergio Rodríguez
# ============================================================

def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN block'''
    p[0] = ('while', p[3], p[5])

def p_parameter_list(p):
    '''parameter_list : variable_list
                      | empty'''
    p[0] = p[1] if p[1] else []

def p_variable_list(p):
    '''variable_list : variable_list COMMA VARIABLE
                     | VARIABLE'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_function_definition(p):
    '''function_definition : FUNCTION ID LPAREN parameter_list RPAREN block'''
    p[0] = ('function_def', p[2], p[4], p[6])

precedence = (
    ('left', 'LOR'),
    ('left', 'LAND'),
    ('nonassoc', 'EQ', 'NOT_EQ', 'LT', 'GT', 'LTE', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    ('right', 'POW'),
    ('right', 'EQUALS'),
    ('right', 'UMINUS', 'LNOT'), 
    ('left', 'INC', 'DEC'),
)

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MODULO expression
                  | expression POW expression
                  | expression EQ expression
                  | expression NOT_EQ expression
                  | expression LT expression
                  | expression GT expression
                  | expression LTE expression
                  | expression GTE expression
                  | expression LAND expression
                  | expression LOR expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_unary(p):
    '''expression : MINUS expression %prec UMINUS
                  | LNOT expression'''
    p[0] = ('unary', p[1], p[2])

def p_expression_inc_dec(p):
    '''expression : VARIABLE INC
                  | VARIABLE DEC'''
    p[0] = ('incdec', p[2], p[1])
    
def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_literals(p):
    '''expression : NUMBER
                  | FLOAT
                  | STRING
                  | TRUE
                  | FALSE
                  | NULL'''
    p[0] = ('literal', p[1])

def p_expression_variable(p):
    '''expression : VARIABLE'''
    p[0] = ('variable', p[1])

# Estructura de Datos: Array (como expresión)
def p_expression_array(p):
    '''expression : LBRACKET array_elements RBRACKET'''
    p[0] = ('array', p[2])

# Reglas auxiliares para el array
def p_array_elements(p):
    '''array_elements : expression_list
                      | empty'''
    p[0] = p[1]

def p_expression_list(p):
    '''expression_list : expression_list COMMA expression
                       | expression'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]
# ============================================================
# INTEGRANTE 3 - Bryan Zhang
# ============================================================

def p_optional_expression(p):
    '''optional_expression : expression
                           | empty'''
    p[0] = p[1]

def p_for_statement(p):
    '''for_statement : FOR LPAREN optional_expression SEMI optional_expression SEMI optional_expression RPAREN block'''
    p[0] = ('for', p[3], p[5], p[7], p[9])

def p_return_statement(p):
    '''return_statement : RETURN optional_expression SEMI'''
    p[0] = ('return', p[2])

def p_expression_new_object(p):
    '''expression : NEW ID LPAREN array_elements RPAREN
                  | NEW ID'''
    if len(p) == 6:
        p[0] = ('new_object', p[2], p[4])
    else:
        p[0] = ('new_object', p[2], [])

def p_expression_function_call(p):
    '''expression : ID LPAREN array_elements RPAREN'''
    p[0] = ('function_call', p[1], p[3])

def p_expression_array_access(p):
    '''expression : VARIABLE LBRACKET expression RBRACKET'''
    p[0] = ('array_access', p[1], p[3])

# ============================================================
# ============================================================

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
    ejecutar_parser("algoritmo3.php", "bgzhangg")
