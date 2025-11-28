# Analizador Léxico PHP con PLY

## Descripción
Proyecto académico que implementa un **analizador para el lenguaje PHP** utilizando la librería **PLY (Python Lex-Yacc)**.  
El objetivo es identificar tokens básicos del lenguaje y generar un archivo de log con los resultados del análisis.
El sistema es capaz de realizar las tres fases fundamentales de análisis:
Análisis Léxico: Identificación de tokens (palabras reservadas, operadores, variables, literales).
Análisis Sintáctico: Validación de la gramática (estructuras de control, definiciones de clases/funciones, expresiones).
Análisis Semántico: Validación de reglas de contexto (scopes, declaración de variables, conteo de argumentos en funciones y detección de redeclaraciones).

---

## Integrantes
| Nombre          | Rol           | Contribución |
|-----------------|----------------|---------------|
| **Angie Alfonso** | Integrante 1 | Base del proyecto y GUI. Estructura principal del Lexer. En el Parser: estructuras de control (if/else), definición de clases (class) y bloques básicos. En Semántico: Tablas globales de clases y funciones. |
| **Sergio Rodriguez** | Integrante 2 | Manejo de Scopes y Variables. En el Lexer: literales (números, strings, variables). En el Parser: bucles while y definiciones de funciones. En Semántico: Implementación de la SymbolTable para manejo de ámbitos y verificación de variables no declaradas. |
| **Bryan Zhang** | Integrante 3 | Expresiones y Validaciones. En el Lexer: Operadores. En el Parser: Expresiones aritméticas, arrays, bucles for y return. En Semántico: Validación de llamadas a funciones (conteo de argumentos) y asignaciones. |

---

## Estructura del repositorio
```text
Implementacion_Estructura_PHP/
│
├── interfaz.py           # Interfaz Gráfica (GUI) principal para ejecutar el analizador
├── lexer.py              # Analizador Léxico (Tokens y Expresiones Regulares)
├── parser.py             # Analizador Sintáctico (Gramática y AST)
├── semantic.py           # Analizador Semántico (Scopes, Tipos y Lógica)
│
├── algoritmo1.php        # Archivo de prueba (Clases y condicionales básicos)
├── algoritmo2.php        # Archivo de prueba (Operaciones, funciones y strings)
├── algoritmo3.php        # Archivo de prueba (Bucles for, arrays y recursividad)
├── algoritmo_semantico.php   # Pruebas específicas de errores semánticos (Scopes)
├── algoritmo_semantico_2.php # Pruebas de conteo de argumentos y funciones
│
├── logs/                 # Carpeta donde se generan los reportes de ejecución (.txt)
└── README.md             # Documentación del proyecto
```
---

## Dependencias
- **Python** ≥ 3.8  
- **PLY** ≥ 3.11
- **Tkinter**

▶ Instalación rápida:
```bash
pip install ply
```
▶ Ejecución
```bash
python interfaz.py
```

Ejecutar el analizador:

python lexer.py
El log generado se guardará automáticamente en la carpeta logs/, con el formato:

lexico-usuarioGit-fecha-hora.txt

Ejemplo de salida
Log generado: logs/lexico-angie329-12-11-2025-17h29.txt
