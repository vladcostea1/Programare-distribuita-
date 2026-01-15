def run_length_encoding(text):
    try:
        if not isinstance(text, str):
            raise TypeError
        if text == "":
            return ""
        result = []
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                result.append(text[i - 1] + str(count))
                count = 1
        result.append(text[-1] + str(count))
        return "".join(result)
    except TypeError:
        return ""
    except Exception:
        return ""

text = "aaabbbbcccdde"
print(run_length_encoding(text))
