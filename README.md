# Analizador Léxico PHP con PLY

## Descripción
Proyecto académico que implementa un **analizador léxico para el lenguaje PHP** utilizando la librería **PLY (Python Lex-Yacc)**.  
El objetivo es identificar tokens básicos del lenguaje y generar un archivo de log con los resultados del análisis.

---

## Integrantes
| Nombre          | Rol           | Contribución |
|-----------------|----------------|---------------|
| **Angie Alfonso** | Integrante 1 | Implementación base del lexer, definición de palabras reservadas, manejo de comentarios y función de logging |

---

##  Estructura del repositorio
Implementacion_Estructura_PHP/
│
├── lexer.py # Archivo principal del analizador léxico
├── algoritmo1.php # Archivo de prueba PHP (Angie Alfonso)
├── logs/ # Carpeta donde se generan los archivos de log
└── README.md # Documento descriptivo del proyecto

---

## Dependencias
- **Python** ≥ 3.8  
- **PLY** ≥ 3.11  

Instalación rápida:
```bash
pip install ply

▶ Ejecución
Crear entorno virtual :

python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

Ejecutar el analizador:

python lexer.py
El log generado se guardará automáticamente en la carpeta logs/, con el formato:

lexico-usuarioGit-fecha-hora.txt

Ejemplo de salida
Log generado: logs/lexico-angie329-12-11-2025-17h29.txt