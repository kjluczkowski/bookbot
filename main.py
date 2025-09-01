from stats import count_words, count_chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    word_count = count_words(text)

    character_count = count_chars(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    char_dict = {}
    char_list = []

    for key,value in character_count.items():
        char_dict = {"char": key, "num": value}
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)
    
    for val in char_list:
        ch = val["char"]
        if ch.isalpha():
            print(f"{ch}: {val["num"]}")

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(items):
    return items["num"]


main()