def analiza_dataset(df):
    try:
        if df is None or df.empty:
            raise ValueError("Dataset invalid!")

        print("\nSTATISTICI GENERALE:")
        print(df[["pret", "cantitate", "profit"]].agg(["mean", "max", "min"]))

        print("\nTotal vanzari:", df["venit"].sum())
        print("Profit total:", df["profit"].sum())

        # evolutie zilnica
        zilnic = df.groupby("data")[["venit", "profit"]].sum()
        print("\nEvolutie zilnica:\n", zilnic.head())

        # distributii
        distributii = {
            "preturi": df["pret"].describe(),
            "cantitati": df["cantitate"].describe()
        }

        print("\nDistributii:\n", distributii)

        # impact promotii
        promotii = df[df["promotie"] == True]
        print("\nImpact promotii:")
        print(promotii[["pret", "venit"]].describe())

    except ValueError as ve:
        print("Eroare:", ve)
    except Exception as e:
        print("Eroare neasteptata:", e)


# APEL
from simulareVanzari import genereaza_dataset
df = genereaza_dataset()
analiza_dataset(df)