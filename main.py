from stats import count_words, count_chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    word_count = count_words(text)

    character_count = count_chars(text)

    print(f"{word_count} words found in the document")

    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()