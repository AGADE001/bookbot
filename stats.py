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
    