import pytest
from ..src.validator import validate
'''
At least 1 lowercase character
At least 1 uppercase character
At least 1 number
At least 1 underscore, dash, comma, or slash
Password must be at least 6 characters long
Max 12 characters long

X Abc-12 -> True

X ABC-12 -> False

X abc-12 -> False

X Abc--- -> False
X Abc-09 -> True

X Abc+12 -> False

X Abc_12 -> true
X Abc,12 -> true
X Abc/12 -> true

X Abc-1 -> False

X Abc-12abc-12- -> False

Additional requirement: A password cannot contain the same phrase twice
Definition of a phrase? => min 3 chars builds a phrase 

Abc-12aaa -> False

'''


def test_ok_password():
    assert validate('Abc-12') == True


def test_no_lowercase_character():
    assert validate('ABC-12') == False


def test_no_uppercase_character():
    assert validate('abc-12') == False


def test_no_numbers():
    assert validate('Abc---') == False


def test_other_numbers():
    assert validate('Abc-09') == True


def test_must_allow_dash():
    assert validate('Abc+12') == False


def test_must_allow_underscore():
    assert validate('Abc_12') == True


def test_must_allow_comma():
    assert validate('Abc,12') == True


def test_must_allow_slash():
    assert validate('Abc/12') == True


def test_must_contain_at_least_6_characters():
    assert validate('Abc-1') == False


def test_must_contain_max_12_characters():
    assert validate('Abc-12abc-12-') == False
