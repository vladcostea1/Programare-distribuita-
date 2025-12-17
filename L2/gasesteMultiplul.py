while True:
    try:
        x = int(input("Introdu numărul x: "))
        y = int(input("Introdu numărul y: "))

        if x <= 0 or y <= 0:
            print("Valorile trebuie să fie numere pozitive. Mai incearca.")
            continue

        if x >= y:
            print("x trebuie să fie mai mic decât y. Mai incearca.")
            continue

        multiplu = x
        while multiplu < y:
            print(multiplu)
            multiplu += x

        break  # ieșire doar când totul este valid

    except ValueError:
        print(" Introdu doar numere întregi.")
