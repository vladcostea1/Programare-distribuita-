import random

numar_secret = random.randint(1, 20)
incercari_ramase = 5

print("Am ales un număr între 1 și 20. Ai 5 încercări.")

while incercari_ramase > 0:
    try:
        ghicire = int(input("Introdu numărul tău: "))

        if ghicire < 1 or ghicire > 20:
            print("Numărul trebuie să fie între 1 și 20.")
            continue

        incercari_ramase -= 1

        if ghicire < numar_secret:
            print("Prea mic.")
        elif ghicire > numar_secret:
            print("Prea mare.")
        else:
            print("Corect! Ai ghicit numărul.")
            break

        print(f"Încercări rămase: {incercari_ramase}")

    except ValueError:
        print("Introdu un număr valid.")

if incercari_ramase == 0:
    print(f"Ai pierdut! Numarul era {numar_secret}.")
