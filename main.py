from stats import count_words,count_characters,sort_dictionary
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def print_report(path_to_file):
    character_dictionary = count_characters(get_book_text(path_to_file))
    sorted_characters = sort_dictionary(character_dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(path_to_file))} total words")
    print("----------- Character Count ----------")

    for characters in sorted_characters:
        dict_key = next(iter(characters))
        dict_value = characters[dict_key]

        if dict_key.isalpha():
            print(f"{dict_key}: {dict_value}")

    print("============= END ===============")

def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_report(sys.argv[1])




main()

