def count_words(text):
    array_of_words = text.split()
    return len(array_of_words)

def count_characters(text):

    character_frequency = {}

    for character in text :
        lower_case_character = character.lower()
        if lower_case_character in character_frequency:
            character_frequency[lower_case_character] += 1
        else:
            character_frequency[lower_case_character] = 1

    return character_frequency

def sort_on(dictionary):
    return dictionary["num"]

def sort_dictionary(character_dictionary):
    list = []
    for key in character_dictionary:
        num = character_dictionary[key]
        new_dictionary = {key:character_dictionary[key],"num":num}

        list.append(new_dictionary)

    list.sort(key=sort_on, reverse=True)

    return list