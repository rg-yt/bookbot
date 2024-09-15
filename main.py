def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)



def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_chars_dict(text):
    dictionary = {}
    for chr in text:
        chr = chr.lower()
        if chr in dictionary:
          dictionary[chr] += 1
        else:
          dictionary[chr] = 1
    return dictionary
        


main()
