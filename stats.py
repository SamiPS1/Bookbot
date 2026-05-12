def word_count(text: str):
    words = text.split()
    return len(words)

def num_characters(text: str):
    char = text.lower()
    word_directory = {}
    for c in char:
        if c in word_directory:
            word_directory[c] += 1
        else:
            word_directory[c] = 1
    return word_directory

def sort_by(word_dict: dict):
    sorted_items = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_items)
    
