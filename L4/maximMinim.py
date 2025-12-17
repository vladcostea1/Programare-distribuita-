while True:
    try:
        text = input("Introdu o listă de numere separate prin virgulă: ")

        valori = text.split(",")
        numere = [int(x.strip()) for x in valori]

        if len(numere) == 0:
            print("Lista nu poate fi goală. Mai încearcă.")
            continue

        print(f"Minimul este: {min(numere)}")
        print(f"Maximul este: {max(numere)}")
        break

    except ValueError:
        print("Introdu doar numere întregi separate prin virgulă.")
