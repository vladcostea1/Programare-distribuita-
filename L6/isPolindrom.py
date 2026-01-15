def is_palindrome(text):
    try:
        if not isinstance(text, str):
            raise TypeError
        cleaned = "".join(text.lower().split())
        return cleaned == cleaned[::-1]
    except TypeError:
        return False
    except Exception:
        return False

text = "A man a plan a canal Panama"
print(is_palindrome(text))
