import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} found in the document")
    print("\n")
    for c in chars_dict:
        print(f"The {c} character was found {chars_dict[c]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    return len(text.split())


def get_chars_dict(text):
    char_dict = {char: 0 for char in string.ascii_lowercase}
    characters = list(text)
    for char in characters:
        if char in char_dict:
            char_dict[char] += 1
    return char_dict


if __name__ == "__main__":
    main()