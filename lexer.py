VOCABULARIO = {
    "I": "PRON",
    "me": "PRON",
    "a": "DET",
    "the": "DET",
    "cat": "NOUN",
    "mat": "NOUN",
    "rat": "NOUN",
    "like": "VERB",
    "is": "VERB",
    "see": "VERB",
    "sees": "VERB",
    ".": "DOT"  # terminal obligatorio
}

def lexer(oracion):
    tokens = []
    palabras = oracion.strip().replace('.', ' .').split()

    for palabra in palabras:
        if palabra in VOCABULARIO:
            tokens.append((VOCABULARIO[palabra], palabra))
        else:
            raise ValueError(f"Error léxico: {palabra}")
    return tokens

if __name__ == "__main__":
    linea = input("Ingrese una oración: ")
    try:
        resultado = lexer(linea)
        print(f"Tokens: {resultado}")
    except ValueError as e:
        print(str(e))
