from stats import get_num_words, get_count_char, convert

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents=f.read()
    return file_contents
def main():
    frank_book=get_book_text("books/frankenstein.txt")
    count=get_num_words(frank_book)
    character_dic=get_count_char(frank_book)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print (f"Found {count} total words")
    print ("--------- Character Count -------")
    for item in convert(character_dic):
        if item["name"].isalpha():
            print(f"{item['name']}: {item['num']}")
    print ("============= END ===============")
    return
main()
