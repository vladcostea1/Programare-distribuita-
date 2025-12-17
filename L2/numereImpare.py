while True:
    try:
        n = int(input("Introdu un număr n: "))

        if n <= 0:
            print("n trebuie să fie un număr pozitiv. Mai încearcă.")
            continue

        for i in range(1, n + 1, 2):
            print(i, end=", ")

        break

    except ValueError:
        print("Introdu un număr întreg valid.")
