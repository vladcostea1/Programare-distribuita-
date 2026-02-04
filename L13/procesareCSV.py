import csv
import os

def proceseaza_comenzi(fisier_intrare, fisier_iesire):
    try:
        if not os.path.exists(fisier_intrare):
            raise FileNotFoundError("Fisierul CSV de intrare nu exista!")

        with open(fisier_intrare, mode="r", newline="", encoding="utf-8") as f_in:
            reader = csv.DictReader(f_in)

            # Verificam coloanele necesare
            coloane_necesare = {"Produs", "Cantitate", "Pret unitar"}
            if not coloane_necesare.issubset(reader.fieldnames):
                raise ValueError("CSV-ul nu contine toate coloanele necesare!")

            with open(fisier_iesire, mode="w", newline="", encoding="utf-8") as f_out:
                fieldnames = ["Produs", "Cantitate", "Pret unitar", "Valoare totala"]
                writer = csv.DictWriter(f_out, fieldnames=fieldnames)
                writer.writeheader()

                for rand in reader:
                    try:
                        produs = rand["Produs"]
                        cantitate = float(rand["Cantitate"])
                        pret = float(rand["Pret unitar"])
                        valoare = cantitate * pret

                        writer.writerow({
                            "Produs": produs,
                            "Cantitate": cantitate,
                            "Pret unitar": pret,
                            "Valoare totala": valoare
                        })

                    except ValueError:
                        print(f"Eroare date invalide pentru produsul: {rand}")

        print("Procesare finalizata cu succes ")

    except FileNotFoundError as e:
        print("EROARE:", e)
    except ValueError as e:
        print("EROARE:", e)
    except Exception as e:
        print("Eroare neasteptata:", e)


# === APEL ===
fisier_intrare = "comenzi.csv"
fisier_iesire = "rezultate.csv"

proceseaza_comenzi(fisier_intrare, fisier_iesire)
