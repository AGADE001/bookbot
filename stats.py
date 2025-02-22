def word_counter(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def character_counter(book_text):
    all_characters = {}

    for char in book_text.lower():
        if char in all_characters:
            all_characters[char] += 1
        else:
            all_characters[char] = 1
    return all_characters

def sort_key(char_dict):
    for key in char_dict:
        return char_dict[key] 

def sort_output(char_dict):
    char_list = []

    for key, value in char_dict.items():
        new_dict = {key: value}
        char_list.append(new_dict)

    char_list.sort(key=sort_key, reverse=True)
    return char_list
    
