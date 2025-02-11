def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(count_words(file_contents))

def count_words(string):
    words = string.split()
    return len(words)


main()