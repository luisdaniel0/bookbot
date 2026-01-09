from stats import get_book_text
import sys


def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path=sys.argv[1]
    print("============ BOOKBOT ============")
    
    print(f"Analyzing book found at {file_path}")
    get_book_text(file_path)
    
    

main()






        
