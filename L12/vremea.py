import requests
import urllib3

# Dezactivare avertizare SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def afiseaza_meteo():
    try:
        oras = input("Introdu numele orasului: ").strip()
        if not oras:
            print("EROARE: Nu ai introdus niciun oras!")
            return

        # Cerere GET la wttr.in (format json)
        url = f"https://wttr.in/{oras}?format=j1"
        response = requests.get(url, verify=False, timeout=10)  # ignore SSL

        if response.status_code != 200:
            print(f"EROARE: API-ul a returnat codul {response.status_code}")
            return

        data = response.json()

        # Verificam daca exista date meteo
        if "current_condition" not in data or not data["current_condition"]:
            print("Orasul nu a fost gasit sau nu exista date meteo.")
            return

        current = data["current_condition"][0]
        vreme = current.get("weatherDesc")[0]["value"] if current.get("weatherDesc") else "Necunoscut"
        temperatura = current.get("temp_C", "Necunoscut")
        vant_directie = current.get("winddir16Point", "Necunoscut")
        vant_viteza = current.get("windspeedKmph", "Necunoscut")

        # Afisare frumoasa
        print("\n--- VREMEA ACTUALA ---")
        print(f"Oras: {oras}")
        print(f"Conditii meteo: {vreme}")
        print(f"Temperatura: {temperatura} °C")
        print(f"Vant: {vant_viteza} km/h, directia {vant_directie}")

    except requests.exceptions.RequestException as e:
        print("EROARE la conectarea la API:", e)
    except Exception as e:
        print("A aparut o eroare:", e)

# === APEL ===
afiseaza_meteo()
