def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        content = f.read()
    count_words(content)
    count_characters(content)

def count_words(content):
    words = len(content.split())
    print(f"{words} words are found in the document")

def count_characters(content):
    characters_dict = {}
    content_lower_case_list = list([c for c in content.lower() if c.isalpha()])

    for c in content_lower_case_list:
        if c not in characters_dict:
            characters_dict[c] = 1
        else:
            characters_dict[c] += 1

    sorted_dict = {k: v for k, v in sorted(characters_dict.items(), key = lambda x: x[1], reverse = True)}
    
    for k, v in sorted_dict.items():
        print(f"The '{k}' character was found {v} times")

main()
