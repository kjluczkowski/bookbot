def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_count = {}
    for char in text:
        lchar = char.lower()
        if lchar in char_count:
            char_count[lchar] += 1
        else:
            char_count[lchar] = 1
    return char_count