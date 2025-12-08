while True:
    principal = input("Introdu principalul: ").strip()
    rate = input("Introdu rata anuala a dobanzii (ex: 5, 6, 10): ").strip()
    time = input("Introdu timpul in ani: ").strip()

    if not (principal.replace('.', '', 1).isdigit() and
            rate.replace('.', '', 1).isdigit() and
            time.replace('.', '', 1).isdigit()):
        print("Te rog sa introduci doar numere reale pozitive.")
        continue

    principal = float(principal)
    rate = float(rate)
    time = float(time)

    interest = (principal * rate * time) / 10
    print(f"Dobanda calculata este: {interest}")
    break
