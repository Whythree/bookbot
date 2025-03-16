from stats import count_words,count_characters,sort_dictionary


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def print_report():
    print("============ BOOKBOT ============")


def main():
    #print(f"{count_words(get_book_text('./books/frankenstein.txt'))} words found in the document.")
    character_dictionary = count_characters(get_book_text('./books/frankenstein.txt'))
    sort_dictionary(character_dictionary)



main()

