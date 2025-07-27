from stats import get_num_words, get_count_char, convert
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents=f.read()
    return file_contents
def main():

    if len (sys.argv) !=2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path=sys.argv[1]
    frank_book=get_book_text(path)
    count=get_num_words(frank_book)
    character_dic=get_count_char(frank_book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print (f"Found {count} total words")
    print ("--------- Character Count -------")
    for item in convert(character_dic):
        if item["name"].isalpha():
            print(f"{item['name']}: {item['num']}")
    print ("============= END ===============")
    return
main()

