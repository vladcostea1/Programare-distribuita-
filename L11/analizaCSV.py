import pandas as pd

def analiza_vanzari_csv():
    try:
        # 1. Citire CSV
        df = pd.read_csv("vanzari.csv")

        # 2. Verificare coloane
        coloane_necesare = {"produs", "cantitate", "pret", "data_vanzarii"}
        if not coloane_necesare.issubset(df.columns):
            raise ValueError("CSV-ul nu contine toate coloanele necesare!")

        # 3. Conversii
        df["data_vanzarii"] = pd.to_datetime(df["data_vanzarii"], errors="raise")
        df["cantitate"] = pd.to_numeric(df["cantitate"], errors="raise")
        df["pret"] = pd.to_numeric(df["pret"], errors="raise")

        # 4. Calcul venit
        df["venit"] = df["cantitate"] * df["pret"]



        # Cele mai vandute produse pe luna
        print("\n Produse vandute pe luna ")
        produse_luna = (
            df.groupby([df["data_vanzarii"].dt.to_period("M"), "produs"])["cantitate"]
            .sum()
        )
        print(produse_luna)

        # Venit total pe produs
        print("\n Venit total pe produs ")
        venit_produs = df.groupby("produs")["venit"].sum()
        print(venit_produs)

        # Filtrare interval
        print("\n Vanzari intre 01.01.2024 si 31.03.2024 ")
        filtrat = df[
            (df["data_vanzarii"] >= "2024-01-01") &
            (df["data_vanzarii"] <= "2024-03-31")
        ]
        print(filtrat)

        # Venit mediu lunar
        print("\n--- Venit mediu lunar ---")
        venit_mediu_lunar = (
            df.groupby(df["data_vanzarii"].dt.to_period("M"))["venit"]
            .mean()
        )
        print(venit_mediu_lunar)

    except FileNotFoundError:
        print("EROARE: Fisierul vanzari.csv NU exista in folder!")
    except ValueError as ve:
        print("EROARE CSV:", ve)
    except Exception as e:
        print("EROARE neasteptata:", e)


#  APEL OBLIGATORIU
analiza_vanzari_csv()