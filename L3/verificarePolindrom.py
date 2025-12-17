def is_palindrome(word):
    return word == word[::-1]


while True:
    cuvant = input("Introdu un cuvânt: ").strip()

    if cuvant == "":
        print("Cuvântul nu poate fi gol. Mai încearcă.")
        continue

    if is_palindrome(cuvant):
        print("Cuvântul este palindrom.")
    else:
        print("Cuvântul NU este palindrom.")

    break
