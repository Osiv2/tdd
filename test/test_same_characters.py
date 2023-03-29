import pytest
from ..src.is_same_character import is_same_character

'''

Additional requirement: A password cannot contain the same character three times in a row (a and A is not the same character).

aaa -> True
'''


def test_same_character():
    assert is_same_character('aaa') == True
