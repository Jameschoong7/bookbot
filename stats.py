def count_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words


def count_characters(text):
    characters_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in characters_dict:
            characters_dict[char] = 1
        else:
            characters_dict[char] +=1
    return characters_dict

def sort_on(items):
    return items["num"]

def sort_characters_count(characters_dict):
    character_dict_list = []
    
    for char in characters_dict:
        temp_dict={}
        
        temp_dict["char"] = char
        temp_dict["num"] = characters_dict[char]
        character_dict_list.append(temp_dict)
    
    character_dict_list.sort(reverse = True, key = sort_on)
    return character_dict_list