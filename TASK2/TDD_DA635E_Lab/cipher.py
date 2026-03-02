def cipher_function(text):
    #if word is None or empty, return unchanged
    if text is None:
        return None

    if text == "":
        return ""

    #only transform alphabetic words, if numerical return unchanged
    if not text.isalpha():
        return text

    word_lower = text.lower()

    #Rule 1: Palindrome (highest priority)
    if is_palindrome(word_lower):
        return text

    #Rule 2: Contains repeated letters  (medium priority)
    if has_repeated_letters(word_lower):
        return reverse_word(text)

    #Rule 3: All unique letters (lowest priority)
    return rotate_left(text)


def is_palindrome(word):
    return word == word[::-1]


def has_repeated_letters(word):
    seen = set()
    for ch in word:
        if ch in seen:
            return True
        seen.add(ch)
    return False


def reverse_word(word):
    return word[::-1]


def rotate_left(word):
    return word[1:] + word[0]