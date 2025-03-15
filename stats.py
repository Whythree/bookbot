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
