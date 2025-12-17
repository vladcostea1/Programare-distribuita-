while True:
    try:
        text = input("Introdu valori separate prin virgulă: ")
        valori = text.split(",")
        tupla = tuple(x.strip() for x in valori)

        if len(tupla) == 0:
            print("Tupla nu poate fi goală. Mai încearcă.")
            continue

        while True:
            cauta = input("Introdu valoarea de căutat: ").strip()

            if cauta in tupla:
                index = tupla.index(cauta)
                print(f"{cauta} se regăsește în tuplă la indexul {index}.")
                break
            else:
                print(f"{cauta} NU se regăsește în tuplă. Mai încearcă.")

        print(f"Tupla finală: {tupla}")
        break

    except Exception:
        print("A apărut o eroare. Mai încearcă.")
