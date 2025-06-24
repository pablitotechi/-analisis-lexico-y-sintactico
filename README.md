# 🧠 Proyecto Programado 1 — Paradigmas de programación

> **Estudiantes:** Pablo Garro y Rodrigo Vásquez  
> **Curso:** Paradigmas de programación 
> **Año:** 2025

---

## 📌 Descripción

Este proyecto implementa un analizador **léxico** y **sintáctico** para un lenguaje artificial reducido llamado **Little English**.

El programa lee oraciones desde un archivo de entrada, y por cada línea realiza:

- ✅ **Análisis léxico:** convierte palabras en tokens válidos o lanza errores.
- ✅ **Análisis sintáctico:** valida que los tokens respeten la gramática del lenguaje.
- 📝 **Registro del resultado:** escribe en un archivo de salida si la línea es válida o tiene errores.

---

## 📁 Estructura del Proyecto

proyecto/
├── lexer.py # Analizador léxico
├── parser.py # Analizador sintáctico
├── main.py # Coordinador principal
├── entrada.txt # Archivo de entrada (oraciones)
├── salida.txt # Archivo de salida (resultados)


🧪 Comportamiento del Programa
Por cada línea en el archivo de entrada:

🧩 Se ejecuta el análisis léxico (lexer.py):

Devuelve una lista de tokens o lanza un error si alguna palabra no es reconocida.

🧠 Se ejecuta el análisis sintáctico (parser.py):

Revisa que los tokens formen una oración válida según la gramática.

📤 Se registra el resultado en el archivo de salida (salida.txt):

✅ Si todo está correcto.

❌ Si hay error léxico o sintáctico.
