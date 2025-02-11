def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    print_report(book_path,num_words,sort_dict(num_characters))

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    char_dict = {}
    for char in string.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    list_of_dict = [{"char":k, "count":v} for k,v in dict.items()]
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict



def print_report(path,num_words, char_dict_list):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for item in char_dict_list:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
        
            



main()