def reverse_words(sentence):
    try:
        if not isinstance(sentence, str):
            raise TypeError
        words = sentence.split()
        return " ".join(words[::-1])
    except TypeError:
        return ""
    except Exception:
        return ""

text = "soricel un cu joaca se pisica"
print(reverse_words(text))
