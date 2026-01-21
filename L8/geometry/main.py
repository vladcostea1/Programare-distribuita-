from circle import aria_cercului, circumferinta_cercului
from rectangle import aria_dreptunghiului, perimetru_dreptunghiului

try:
    print("Aria cercului:", aria_cercului(5))
    print("Circumferința cercului:", circumferinta_cercului(5))

    print("Aria dreptunghiului:", aria_dreptunghiului(4, 6))
    print("Perimetrul dreptunghiului:", perimetru_dreptunghiului(4, 6))

except ValueError as e:
    print("Eroare:", e)
