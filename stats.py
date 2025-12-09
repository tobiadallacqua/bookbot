def get_num_words(book_text):
    num_words = book_text.split()
    return len(num_words)


def get_num_appearances(book_text):
    lower_book_text = book_text.lower()
    characters_count = {}
    characters_done = []
    for c in lower_book_text:
        if c not in characters_done:
            counter = 0
            characters_done.append(c)
            for letter in lower_book_text:
                if letter == c:
                    counter += 1
            characters_count[c] = counter
        else:
            continue
    # print(characters_done)
    # print(characters_count["o"])
    return characters_count


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]


def sort_items(characters_dict):
    list_of_dictionaries = []
    for i in characters_dict:
        list_of_dictionaries.append({"char": i, "num": characters_dict[i]})
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries
