import os

def redenumire_fisiere(folder_path):
    try:
        # Verificare daca directorul exista
        if not os.path.exists(folder_path):
            raise FileNotFoundError("Directorul specificat nu exista!")

        # Lista tuturor elementelor din director
        fisiere = os.listdir(folder_path)

        if not fisiere:
            print("Directorul este gol.")
            return

        for nume_fisier in fisiere:
            cale_veche = os.path.join(folder_path, nume_fisier)

            # Verificam daca este fisier (nu director)
            if os.path.isfile(cale_veche):
                # Evitam redenumirea repetata
                if not nume_fisier.startswith("renamed_"):
                    nume_nou = "renamed_" + nume_fisier
                    cale_noua = os.path.join(folder_path, nume_nou)

                    try:
                        os.rename(cale_veche, cale_noua)
                        print(f"Redenumit: {nume_fisier} → {nume_nou}")
                    except PermissionError:
                        print(f"Eroare permisiuni pentru fisierul: {nume_fisier}")
                    except OSError as e:
                        print(f"Eroare la redenumirea fisierului {nume_fisier}: {e}")
                else:
                    print(f"Fisier deja redenumit: {nume_fisier}")

        print("\nRedenumire finalizata cu succes ✔️")

    except FileNotFoundError as e:
        print("EROARE:", e)
    except Exception as e:
        print("A aparut o eroare neasteptata:", e)


# === APEL FUNCTIE ===
folder = r"C:\Users\vladc\PycharmProjects\PythonProject\L13"
  # <-- schimba cu calea ta reala
redenumire_fisiere(folder)
