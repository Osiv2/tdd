def validate(password):
    contains_lower_case = False
    contains_upper_case = False

    for c in password:
        if c.islower():
            contains_lower_case = True
        if c.isupper():
            contains_upper_case = True

    if contains_lower_case and contains_upper_case:
        return True
    return False
