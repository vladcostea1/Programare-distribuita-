import requests

def conversie_valutara():
    try:
        # Citire date de la utilizator
        moneda_sursa = input("Introdu moneda de provenienta (ex: RON, EUR, USD): ").upper()
        moneda_dest = input("Introdu moneda de destinatie (ex: EUR, USD, RON): ").upper()
        suma = float(input("Introdu suma de convertit: "))

        # API public
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Nu s-au putut obtine cursurile de schimb.")

        data = response.json()
        rate = data["rates"]

        if moneda_sursa not in rate or moneda_dest not in rate:
            raise ValueError("Moneda introdusa nu este suportata.")

        # Conversie: sursa -> USD -> destinatie
        curs_sursa = rate[moneda_sursa]
        curs_dest = rate[moneda_dest]

        suma_usd = suma / curs_sursa
        suma_finala = suma_usd * curs_dest

        # Afisare rezultat
        print("\n--- REZULTAT CONVERSIE ---")
        print(f"Suma initiala: {suma} {moneda_sursa}")
        print(f"Curs {moneda_sursa} -> USD: {1 / curs_sursa:.4f}")
        print(f"Curs USD -> {moneda_dest}: {curs_dest:.4f}")
        print(f"Suma finala: {suma_finala:.2f} {moneda_dest}")

    except ValueError as e:
        print("EROARE:", e)
    except Exception as e:
        print("EROARE:", e)


# === APEL ===
conversie_valutara()
