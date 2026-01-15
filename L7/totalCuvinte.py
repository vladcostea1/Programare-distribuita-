def count_words_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        return len(content.split())
    except Exception:
        return 0

print(count_words_in_file("sir.txt"))
