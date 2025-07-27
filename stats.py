def get_num_words(text):
    return len(text.split())
def get_count_char(input_text):
    char_dic={}
    count=0
    for char in input_text.lower():
        if char in char_dic:
            char_dic[char] +=1
        else:
            char_dic[char]=1
    
    return char_dic
def sort_on(items):
    return items["num"]
def convert(data):
    char_list=[{"name":key, "num":value} for key, value in data.items()]
    sort_list=sorted(char_list, key=sort_on, reverse=True)
    return sort_list
