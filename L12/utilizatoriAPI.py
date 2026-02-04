import requests
from tabulate import tabulate

def afiseaza_utilizatori(oras_filtru=None):
    try:
        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            raise Exception(f"API-ul a returnat codul: {response.status_code}")

        utilizatori = response.json()

        tabel = []
        for user in utilizatori:
            id_user = user.get("id")
            nume = user.get("name")
            username = user.get("username")
            email = user.get("email")
            oras = user.get("address", {}).get("city")
            companie = user.get("company", {}).get("name")
            telefon = user.get("phone")
            website = user.get("website")

            # Filtrare dupa oras daca se specifica
            if oras_filtru:
                if oras.lower() != oras_filtru.lower():
                    continue

            tabel.append([id_user, nume, username, email, oras, companie, telefon, website])

        if tabel:
            headers = ["ID", "Nume", "Username", "Email", "Oras", "Companie", "Telefon", "Website"]
            print(tabulate(tabel, headers=headers, tablefmt="grid"))
        else:
            print(f"Nu s-au gasit utilizatori din orasul '{oras_filtru}'.")

    except requests.exceptions.RequestException as e:
        print("EROARE la conectarea cu API-ul:", e)
    except Exception as e:
        print("A aparut o eroare:", e)


# === APEL ===
# Pentru a afisa TOTI utilizatorii
afiseaza_utilizatori()

# Pentru a filtra dupa oras (ex: Gwenborough)
# afiseaza_utilizatori("Gwenborough")
