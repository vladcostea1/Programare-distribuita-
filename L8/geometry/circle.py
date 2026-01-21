import math

def aria_cercului(raza):
    if raza <= 0:
        raise ValueError("Raza trebuie să fie pozitivă.")
    return math.pi * raza ** 2


def circumferinta_cercului(raza):
    if raza <= 0:
        raise ValueError("Raza trebuie să fie pozitivă.")
    return 2 * math.pi * raza
