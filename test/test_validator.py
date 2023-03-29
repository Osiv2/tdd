import pytest
from ..src.validator import validate
'''
At least 1 lowercase character
At least 1 uppercase character
At least 1 number
At least 1 underscore, dash, comma, or slash
Password must be at least 6 characters long
Max 12 characters long

Abc-123 -> 


a -> true
A -> true
1 -> true

'''


def test_lowercase_character():
    assert validate('a') == True
