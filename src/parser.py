def parse(query):
    if query is None or query == "":
        return []
    return list(set(query.split()))
