import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def genereaza_dataset():
    try:
        np.random.seed(42)
        zile = 60
        start = datetime(2024, 1, 1)
        date = []

        for zi in range(zile):
            data = start + timedelta(days=zi)
            nr_produse = np.random.randint(5, 16)

            for _ in range(nr_produse):
                pret = max(1, np.random.normal(40, 8))
                cantitate = np.random.randint(1, 11)

                promotie = np.random.rand() < 0.3
                if promotie:
                    pret *= 0.8

                venit = pret * cantitate
                profit = venit * 0.3

                date.append([data, pret, cantitate, venit, profit, promotie])

        df = pd.DataFrame(date, columns=[
            "data", "pret", "cantitate", "venit", "profit", "promotie"
        ])

        return df

    except Exception as e:
        print("Eroare la generare dataset:", e)
        return None


df = genereaza_dataset()
print(df.head())