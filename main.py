from stats import word_counter, character_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = word_counter(book_text)
    print(f"{word_count} words found in the document")
    
    character_dict = character_counter(book_text)
    for key, value in character_dict.items():
        print(f"'{key}': {value}")
main()
