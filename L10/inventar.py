inventar = {}

def adauga_produs():
    try:
        nume = input("Nume produs: ")
        cantitate = int(input("Cantitate: "))
        inventar[nume] = cantitate
        print("Produs adaugat")
    except ValueError:
        print("Eroare: Cantitatea trebuie sa fie numar intreg!")

def cauta_produs():
    nume = input("Nume produs cautat: ")
    try:
        print("Cantitate:", inventar[nume])
    except KeyError:
        print("Eroare: Produs inexistent!")

def actualizeaza_cantitate():
    try:
        nume = input("Nume produs: ")
        if nume not in inventar:
            raise KeyError
        cantitate = int(input("Noua cantitate: "))
        inventar[nume] = cantitate
        print("Cantitate actualizata")
    except ValueError:
        print("Eroare: Cantitate invalida!")
    except KeyError:
        print("Eroare: Produs inexistent!")

def meniu():
    while True:
        print("\n MENIU INVENTAR")
        print("1. Adauga produs")
        print("2. Cauta produs")
        print("3. Actualizeaza cantitate")
        print("4. Iesire")

        optiune = input("Alege optiunea: ")

        if optiune == "1":
            adauga_produs()
        elif optiune == "2":
            cauta_produs()
        elif optiune == "3":
            actualizeaza_cantitate()
        elif optiune == "4":
            print("La revedere")
            break
        else:
            print("Optiune invalida!")



meniu()