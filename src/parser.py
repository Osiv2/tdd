def parse(query):
    if query is None:
        return []

    search_engine_query = [parse_word(word) for word in query.split()]
    search_engine_query = [
        word for word in search_engine_query if word is not '']

    return get_unique_list(search_engine_query)


def parse_word(word):
    word = word.lower()
    word = clean_word(word)
    if word in ["in", "at", "on"]:
        word = ""
    if word.endswith('s'):
        word = word[:-1]
    for synonym in synonyms:
        if word in synonym:
            word = synonym[0]
    return word


def get_unique_list(li):
    return list(dict.fromkeys(li))


def clean_word(word):
    new_word = ""
    for char in word:
        if char.isalpha():
            new_word += char
    return new_word


synonyms = [("developer", "coder", "programmer"), ("berliner", "donut")]
