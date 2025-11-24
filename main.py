from stats import count_words, char_count, sort_character_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")
    print_report(book_path)

def get_book_text(filepath):
    with open(filepath) as file:
        file_content = file.read()
    return file_content

def print_report(book_path):
    text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    list = sort_character_list(char_count(text))
    for char in list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
    
       
main()