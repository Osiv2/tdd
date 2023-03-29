import pytest
from ..src.validator import validate
'''
At least 1 lowercase character
At least 1 uppercase character
At least 1 number
At least 1 underscore, dash, comma, or slash
Password must be at least 6 characters long
Max 12 characters long

Abc-12 -> True

ABC-12 -> False

abc-12 -> False

Abc--- -> False
Abc-09 -> True

Abc_12 -> true
Abc,12 -> true
Abc/12 -> true

Abc-1 -> False

Abc-12abc-12- -> False

'''


def test_ok_password():
    assert validate('Abc-12') == True


def test_no_lowercase_character():
    assert validate('ABC-12') == False
