def reverse_lines():
    try:
        with open("input.txt", "r", encoding="utf-8") as fin:
            lines = fin.readlines()
        with open("output.txt", "w", encoding="utf-8") as fout:
            for line in lines:
                fout.write(line.rstrip("\n")[::-1] + "\n")
    except Exception:
        print("Eroare: verifică dacă input.txt există în același folder")

reverse_lines()
