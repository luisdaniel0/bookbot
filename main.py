from stats import get_book_text



def main():
    print("============ BOOKBOT ============")
    file_path = "./books/frankenstein.txt"
    print(f"Analyzing book found at {file_path}")
    get_book_text(file_path)
    
    

main()





        