import mathOperations as mo

a = 10
b = 5

try:
    print("Adunare:", mo.adunare(a, b))
    print("Scădere:", mo.scadere(a, b))
    print("Înmulțire:", mo.inmultire(a, b))
    print("Împărțire:", mo.impartire(a, b))
except Exception as e:
    print("Eroare:", e)
