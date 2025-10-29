from stats import count_words, count_characters, sort_characters_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    content = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at{file_path}")
    num_words = count_words(content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    num_chars_dict = count_characters(content)
    print("--------- Character Count -------")
    
    sorted_char_list = sort_characters_count(num_chars_dict)
    for char in sorted_char_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()