def imparte_numere():
    try:
        a = float(input("Introdu primul numar: "))
        b = float(input("Introdu al doilea numar: "))

        rezultat = a / b
        print("Rezultatul impartirii este:", rezultat)

    except ZeroDivisionError:
        print("Eroare: Nu se poate imparti la zero!")

    except ValueError:
        print("Eroare: Trebuie sa introduci numere!")

    except Exception as e:
        print("Eroare neasteptata:", e)


# APELUL FUNCTIEI (OBLIGATORIU!)
imparte_numere()