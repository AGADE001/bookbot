from stats import word_counter, character_counter, sort_output

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def header_output(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")

def main():
    filepath = "books/frankenstein.txt"
    header_output(filepath)
    book_text = get_book_text(filepath)
    word_count = word_counter(book_text)
    print(f"Found {word_count} total words")
    
    character_dict = character_counter(book_text)

    output_list = sort_output(character_dict)

    print("--------- Character Count -------")
    for character in output_list:
        for key, value in character.items():
            if key.isalpha():
                print(f"{key}: {value}")
    print("============= END ===============")
main()
