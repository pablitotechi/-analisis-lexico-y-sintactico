# ================================================
#        🧠 PROYECTO PROGRAMADO 1
#   Estudiantes: Pablo Garro y Rodrigo Vásquez
# ================================================
import sys
from lexer import lexer
from parser import parser

def main():
    if len(sys.argv) == 1:
        archivo_entrada = "entrada.txt"
        archivo_salida = "salida.txt"
    elif len(sys.argv) == 3:
        archivo_entrada = sys.argv[1]
        archivo_salida = sys.argv[2]
    else:
        print("Uso: python main.py <archivo_entrada> <archivo_salida>")
        return

    with open(archivo_entrada, 'r') as f:
        lineas = f.readlines()

    resultados = []

    for numero_linea, linea in enumerate(lineas, start=1):
        oracion = linea.strip()
        if not oracion:
            continue
        try:
            tokens = lexer(oracion)
        except ValueError as e:
            resultados.append(f"Línea {numero_linea}: {oracion}\n\t❌ Error léxico: {e}")
            continue

        try:
            parser(tokens)
            resultados.append(f"Línea {numero_linea}: {oracion}\n\t✅ Análisis exitoso")
        except ValueError as e:
            resultados.append(f"Línea {numero_linea}: {oracion}\n\t❌ Error sintáctico: {e}")

    with open(archivo_salida, 'w') as f:
        for r in resultados:
            f.write(r + '\n')

if __name__ == "__main__":
    main()
