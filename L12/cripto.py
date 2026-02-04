import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def obtine_preturi_crypto():
    try:
        url_api = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
        response = requests.get(url_api, timeout=10)
        response.raise_for_status()  # ridica exceptie daca status != 200

        data = response.json()
        tabel = [
            ["Bitcoin (BTC)", data["bitcoin"]["usd"]],
            ["Ethereum (ETH)", data["ethereum"]["usd"]]
        ]
        print("\n--- Preturi Criptomonede ---")
        print(tabulate(tabel, headers=["Criptomoneda", "Pret USD"], tablefmt="grid"))

    except requests.exceptions.RequestException as e:
        print("EROARE la obtinerea preturilor criptomonedelor:", e)
    except Exception as e:
        print("A aparut o eroare:", e)


def extrage_stiri_coindesk():
    try:
        url_news = "https://www.coindesk.com/"
        response = requests.get(url_news, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Extrage link-urile și titlurile articolelor principale
        stiri = []
        # CoinDesk foloseste articole <a> cu clasa 'card-title' pentru titluri (poate varia)
        for a in soup.find_all("a", class_="card-title", limit=5):
            titlu = a.get_text(strip=True)
            link = a['href']
            # link complet
            if not link.startswith("http"):
                link = "https://www.coindesk.com" + link
            stiri.append((titlu, link))

        print("\n--- Ultimele 5 Stiri CoinDesk ---")
        for idx, (titlu, link) in enumerate(stiri, 1):
            print(f"{idx}. {titlu}\n   {link}")

        if not stiri:
            print("Nu s-au gasit stiri pe CoinDesk.")

    except requests.exceptions.RequestException as e:
        print("EROARE la conectarea la CoinDesk:", e)
    except Exception as e:
        print("A aparut o eroare:", e)


# === APEL ===
obtine_preturi_crypto()
extrage_stiri_coindesk()
