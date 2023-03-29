def parse(query):
    if query is None:
        return []

    search_engine_query = [parse_word(word) for word in query.split()]

    return get_unique_list(search_engine_query)


def parse_word(word):
    word = word.lower()
    new_word = ""
    for i, char in enumerate(word):
        if char.isalpha():
            new_word += word[i]
    word = new_word
    if word.endswith('s'):
        word = word[:-1]
    if word in ["coder", "programmer"]:
        word = "developer"
    return word


def get_unique_list(li):
    return list(dict.fromkeys(li))
