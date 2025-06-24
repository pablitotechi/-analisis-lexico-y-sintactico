def parser(tokens):
    tipos = [token[0] for token in tokens]

    estructuras_validas = [
        ['PRON', 'VERB', 'PRON', 'DOT'],               # I see me.
        ['PRON', 'VERB', 'DET', 'NOUN', 'DOT'],        # I see the rat.
        ['DET', 'NOUN', 'VERB', 'DET', 'NOUN', 'DOT'], # the rat sees the mat.
        ['DET', 'NOUN', 'VERB', 'PRON', 'DOT'],        # the cat sees me.
        ['DET', 'NOUN', 'VERB', 'NOUN', 'DOT'],        # the mat is rat.
        ['PRON', 'VERB', 'NOUN', 'DOT']                # I see rat.
    ]

    if tipos not in estructuras_validas:
        raise ValueError(f"Estructura inválida: {tipos}")

    return True

if __name__ == "__main__":
    ejemplo = [('PRON', 'I'), ('VERB', 'see'), ('PRON', 'me'), ('DOT', '.')]
    try:
        parser(ejemplo)
        print("✅ Análisis sintáctico exitoso")
    except ValueError as e:
        print(f"❌ {e}")

