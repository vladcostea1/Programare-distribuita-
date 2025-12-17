def unique_pair_sum(numbers, target):
    rezultat = set()
    vizitat = set()

    for num in numbers:
        complement = target - num
        if complement in vizitat:
            pereche = tuple(sorted((num, complement)))
            rezultat.add(pereche)
        vizitat.add(num)

    return rezultat


while True:
    try:
        text = input("Introdu o listă de numere separate prin virgulă: ")
        numbers = [int(x.strip()) for x in text.split(",")]

        target = int(input("Introdu valoarea țintă: "))

        perechi = unique_pair_sum(numbers, target)
        print("Perechi unice care dau targetul:", perechi)
        break

    except ValueError:
        print("Introdu doar numere întregi valide. Mai încearcă.")
