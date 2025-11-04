def get_word_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        total_word_count = len(words)
    return total_word_count

def get_character_num(file_path):
    character_dict = {}
    
    with open(file_path) as f:
        file_contents = f.read()
        file_words = file_contents.split()
        #filters out num
        book_text = "".join(file_words)
        book_text_low = book_text.lower()

        for letter in book_text_low:
            if letter in character_dict:
                character_dict[letter] += 1
            else:
                character_dict[letter] = 1
        
        character_dict_sorted = sorted(character_dict.items(), key=lambda item: item[1], reverse=True)
        character_dict_decending = dict(character_dict_sorted)
        final_list = [f"{key}: {value}" for key, value in character_dict_decending.items()]

    return final_list

