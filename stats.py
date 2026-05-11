def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        count = num_chars_dict[char]
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
