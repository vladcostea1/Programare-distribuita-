def factorial(n):
    rezultat = 1
    for i in range(1, n + 1):
        rezultat *= i
    return rezultat


while True:
    try:
        n = int(input("Introdu un număr întreg: "))

        if n < 0:
            print("Factorialul nu este definit pentru numere negative. Mai încearcă.")
            continue

        print(f"Factorialul lui {n} este {factorial(n)}")
        break

    except ValueError:
        print("Introdu un număr întreg valid.")
