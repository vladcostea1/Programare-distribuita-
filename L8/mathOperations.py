def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def impartire(a, b):
    if b == 0:
        raise ZeroDivisionError("Împărțirea la zero nu este permisă.")
    return a / b
