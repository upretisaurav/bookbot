def calculate_word_count(text):
    words = text.split()
    return len(words)

def calculate_character_count(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def character_with_num(char_count):
    char_with_num = []
    for char, count in char_count.items():
        char_with_num.append({"char": char, "num": count})

    def sort_on(d):
        return d["num"]

    char_with_num.sort(key=sort_on, reverse=True)
    return char_with_num
