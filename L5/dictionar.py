import string


def word_frequency(text):
    # Transformăm tot textul în lowercase
    text = text.lower()

    # Eliminăm semnele de punctuație
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Spargem textul în cuvinte
    cuvinte = text.split()

    # Construim dicționarul cu frecvențele
    frecventa = {}
    for cuvant in cuvinte:
        frecventa[cuvant] = frecventa.get(cuvant, 0) + 1

    return frecventa


# Exemplu de utilizare
text = "Ana si Maria au plecat la mare. Maria are rau de mare."
rezultat = word_frequency(text)
print(rezultat)
