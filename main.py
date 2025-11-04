import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]

from stats import get_word_count
from stats import get_character_num

def main():
    word_count = get_word_count(path)
    character_num = get_character_num(path)
    
    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ---------- 
Found {word_count} total words
--------- Character Count -------
""")  
    print(*character_num, sep='\n')
    print("============= END ===============")

# python
if __name__ == "__main__":
    main()

