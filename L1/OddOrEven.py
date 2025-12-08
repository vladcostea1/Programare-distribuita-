while True:
    value = input("Dati un numar: ").strip()

    if value == "":
        print("Nu este introdus niciun numar")
        continue

    # Pentru numere negative
    if value.lstrip("-").isdigit():
        numar = int(value)

        if numar % 2 == 0:
            print(f"{numar} este un numar par")
        else:
            print(f"{numar} este un numar impar")

        break  # Se opreste  loop-ul

    else:
        print("Dati un numar intreg real, nu litere sau simboluri")
