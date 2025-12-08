while True:
    valoare = input("Temperatura în grade Celsius: ").strip()

    if valoare == "":
        print("Nu este introdusa nicio valoare")
        continue

    try:
        celsius = float(valoare)
        fahrenheit = celsius * 9/5 + 32
        print(f"Temperatura în Fahrenheit este: {fahrenheit}")
        break
    except ValueError:
        print("Introdu un număr real")
