def parse(query):
    if query is None or query == "":
        return []
    return query.split()
