from stats import count_words,count_characters


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content



def main():
    print(f"{count_words(get_book_text('./books/frankenstein.txt'))} words found in the document.")
    character_dictionary = count_characters(get_book_text('./books/frankenstein.txt'))
    print(character_dictionary)
main()