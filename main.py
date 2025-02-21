def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(book_text):
    words = book_text.split()
    
    word_count = len(words)

    return word_count
    
        
def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = word_counter(book_text)
    print(f"{word_count} words found in the document")
main()
