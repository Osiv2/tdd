def parse(query):
    if query is None or query == "":
        return []

    search_engine_query = list(dict.fromkeys(query.split()))

    return [parse_word(word) for word in search_engine_query]


def parse_word(word):
    word = word.lower()
    if word[len(word)-1] is 's':
        word = word[:-1]
    return word
