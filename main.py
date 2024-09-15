def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = sort_chars_dict(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for char in sorted_list:
        if not char["chr"].isaplpha():
          print(f"The '{char["chr"]}' character was found {char["num"]} times")

    print(f"--- End report ---")

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

def sort_on(dict):
    return dict["num"]

def sort_chars_dict(dict):
    list = []
    for chr in dict:
          list.append({"chr": chr, "num": dict[chr]})
    list.sort(reverse=True, key=sort_on)
    return list
    
main()
