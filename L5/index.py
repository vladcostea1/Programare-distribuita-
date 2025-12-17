import string


def inverted_index(documents):
    index = {}

    for i, doc in enumerate(documents):
        # Lowercase și eliminare punctuație
        doc_clean = doc.lower().translate(str.maketrans("", "", string.punctuation))
        cuvinte = doc_clean.split()

        for cuvant in cuvinte:
            if cuvant not in index:
                index[cuvant] = set()
            index[cuvant].add(i)

    return index


# Exemplu de utilizare
documents = [
    "pisica a stat pe covor",
    "cainele a stat în ceață",
    "pisica și câinele s-au jucat împreună"
]

index = inverted_index(documents)
print(index)
