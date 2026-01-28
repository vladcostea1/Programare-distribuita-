def suma_din_fisier(nume_fisier):
    suma = 0
    try:
        with open(nume_fisier, "r") as f:
            for linie in f:
                try:
                    numar = float(linie.strip())
                    suma += numar
                except ValueError:
                    print("Valoare invalida ignorata:", linie.strip())
        return suma

    except FileNotFoundError:
        print("Eroare: Fisierul nu exista!")
    except IOError:
        print("Eroare: Problema la citirea fisierului!")


# ===== APELUL FUNCTIEI (OBLIGATORIU) =====
nume_fisier = input("Introdu numele fisierului: ")
rezultat = suma_din_fisier(nume_fisier)

if rezultat is not None:
    print("Suma numerelor este:", rezultat)