def parse(query):
    if query is None or query == "":
        return []

    search_engine_query = [parse_word(word) for word in query.split()]

    return list(dict.fromkeys(search_engine_query))


def parse_word(word):
    word = word.lower()
    if word.endswith('s'):
        word = word[:-1]
    if word in ["coder", "programmer"]:
        word = "developer"
    return word
