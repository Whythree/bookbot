from stats import count_words,count_characters,sort_dictionary


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def print_report():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{count_words(get_book_text('./books/frankenstein.txt'))} words found in the document.")
    print("----------- Character Count ----------")


def main():
    print_report()
    character_dictionary = count_characters(get_book_text('./books/frankenstein.txt'))
    sorted_characters = sort_dictionary(character_dictionary)
    print(sorted_characters)
    # wie komme ich nun an das erste key value pair davon?
    for characters in sorted_characters:
        pass


    # This is the answer?
   # list_of_dicts = [{'key1': 'value1', 'key2': 'value2'}, {'key3': 'value3', 'key4': 'value4'}]

    #for my_dict in list_of_dicts:
     #   first_key = next(iter(my_dict))
      #  first_value = my_dict[first_key]
       # print(f"Key: {first_key}, Value: {first_value}")
        #break  # If you only want the first key-value pair from the first di

main()

