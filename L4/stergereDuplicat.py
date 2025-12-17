while True:
    try:
        text = input("Introdu o listă de numere separate prin virgulă: ")
        valori = text.split(",")
        numere = [int(x.strip()) for x in valori]

        if len(numere) == 0:
            print("Lista nu poate fi goală. Mai încearcă.")
            continue

        # Eliminare duplicate păstrând ordinea
        unice = []
        for n in numere:
            if n not in unice:
                unice.append(n)

        print("Lista cu valori unice:", unice)
        break

    except ValueError:
        print("Introdu doar numere întregi separate prin virgulă. Mai încearcă.")
