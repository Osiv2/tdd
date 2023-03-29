def parse(query):
    if query is None or query == "":
        return []

    search_engine_query = list(dict.fromkeys(query.split()))

    return [parse_word(word) for word in search_engine_query]


def parse_word(word):
    word = word.lower()
    if word.endswith('s'):
        word = word[:-1]
    if word == "coder":
        word = "developer"
    return word
