def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    print(num_characters)

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



main()