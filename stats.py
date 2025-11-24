def count_words(string):
    word_list = string.split()
    return len(word_list)

def char_count(string):
    count_char = {}
    normalized_string = string.lower()
    for char in normalized_string:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    return count_char

def sort_on(item):
    return item["num"] 

def sort_character_list(dict):
    list = []
    for item in dict:
        list.append({"char": item, "num": dict[item]})
    list.sort(reverse=True, key=sort_on)
    return list