def get_num_words(text):
    return len(text.split())

def get_count_per_char(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters
        
def get_sorted_list(dict):
    sorted_list = []
    for key, value in dict.items():
        if key.isalpha():
          sorted_list.append({"char": key, "count": value})
    sorted_list.sort(reverse=True, key=lambda x: x['count'])
    return sorted_list