import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


while True:
    try:
        x1 = float(input("Introdu x1: "))
        y1 = float(input("Introdu y1: "))
        x2 = float(input("Introdu x2: "))
        y2 = float(input("Introdu y2: "))

        dist = distance(x1, y1, x2, y2)
        print(f"Distanța dintre puncte este: {dist}")

        break

    except ValueError:
        print("Introdu doar valori numerice. Mai încearcă.")
