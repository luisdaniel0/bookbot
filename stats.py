def word_count(file):
    split_string = file.split(None)
    print("----------- Word Count ----------")
    print(f"Found {len(split_string)} total words")

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        char_dict = character_count(file_content)
        word_count(file_content)
        char_list = convert_to_list(char_dict)

        char_list.sort(reverse=True,key=sort_on)
        print("--------- Character Count -------")
        for char in char_list:
            
            print(f"{char['char']}: {char['num']}")
        print("============= END ===============")
        

def convert_to_list(char_dictionary):
    char_list = []
    for char in char_dictionary:
        char_dict = {"char": char, "num": char_dictionary[char]}
        char_list.append(char_dict)

    return char_list

def sort_on(items):
    return items["num"]

def character_count(string):
    characters = {}
    lower_cased_string = string.lower()
    for char in lower_cased_string:
        if char.isalpha():
            if char in characters:
             characters[char] +=1
            else:
                characters[char]= 1 
    return characters













    
    








