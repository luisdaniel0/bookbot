def word_count(file):
    split_string = file.split(None)
    print(f"Found {len(split_string)} total words")

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        character_count(file_content)
        
def sort_on(items):
    return items

def character_count(string):
    characters = {}
    lower_cased_string = string.lower()
    for char in lower_cased_string:
        
        if char in characters:
            characters[char] +=1
            print(f"repeated character: {char}")
            
        else:
            characters[char]= 1 

    
    
    characters.sort(reverse=True, key=sort_on)
    print(characters)






