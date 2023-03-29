def parse(query):
    if query is None or query == "":
        return []
    return list(dict.fromkeys(query.split()))
