while True:
    value = input("Introduceti un numar")

    if value == "":
        print("Nu este introdus niciun numar")
        continue

    numar = int(input("Dati un numar: "))

    if numar < 2:
        print("Nu este prim.")
    else:
        este_prim = True
        for i in range(2, int(numar ** 0.5) + 1):
            if numar % i == 0:
                este_prim = False
                break

        if este_prim:
            print("Numarul este prim.")
        else:
            print("Numarul nu este prim.")
