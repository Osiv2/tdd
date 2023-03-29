def parse(query):
    if query is None or query == "":
        return []
    return [word.lower() for word in list(dict.fromkeys(query.split()))]
