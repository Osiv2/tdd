def validate(password):
    lowerCases = [c for c in password if c.islower()]
    upperCases = [c for c in password if c.isupper()]
    if len(lowerCases) and len(upperCases):
        return True
    return False
