import sys
from stats import count_words, count_chars

def main():
    sys.argv

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    
    word_count = count_words(text)

    character_count = count_chars(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
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