def validate(password):
    contains_lower_case = False
    contains_upper_case = False
    contains_digit = False
    contains_dash = False
    valid_length = is_valid_length(password)

    for c in password:
        if c.islower():
            contains_lower_case = True
        if c.isupper():
            contains_upper_case = True
        if c.isdigit():
            contains_digit = True
        if is_special_character(c):
            contains_dash = True

    return is_valid_password(contains_lower_case, contains_upper_case, contains_digit, contains_dash, valid_length)


def is_valid_length(password):
    return len(password) >= 6 and len(password) <= 12


def is_valid_password(contains_lower_case, contains_upper_case, contains_digit, contains_dash, valid_length):
    return contains_lower_case and contains_upper_case and contains_digit and contains_dash and valid_length


def is_special_character(char):
    return char in ["-", "_", ",", "/"]
