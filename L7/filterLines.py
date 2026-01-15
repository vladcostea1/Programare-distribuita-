def filter_lines():
    try:
        with open("filter.txt", "r", encoding="utf-8") as fin:
            lines = fin.readlines()
        with open("filtered.txt", "w", encoding="utf-8") as fout:
            for line in lines:
                if "Python" in line:
                    fout.write(line)
    except Exception:
        print("Eroare: verifică fișierele")

filter_lines()
