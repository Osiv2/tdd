def parse(query):
    if query is None or query == "":
        return []

    search_engine_query = list(dict.fromkeys(query.split()))

    return [word.lower() for word in search_engine_query]
