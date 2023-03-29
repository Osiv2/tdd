def validate(password):
    lowerCases = [c for c in password if c.islower()]
    if len(lowerCases):
        return True
    return False
