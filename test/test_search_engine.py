import pytest
from ..src.parser import parse

'''
getList
get list with multiple words
get list of unique words
lowerCase
plural
synonyms

"developer"				        —> ["developer"]
Null -> []
"" -> []
"cool developer"		        —> ["cool", "developer"]
"cool cool developer"		    —> ["cool", "developer"]
"DeveLoper"				        —> ["developer"]
"developers"                    -> ["developer"]
"coder"                         -> ["developer"]
"coder programmer developer"    -> ["developer"]
"coder programmers developers"  -> ["developer"]

"FinD all coders developer"     —> ["find", "all", "developer"]


'''


def test_parse_single_word():
    data = "developer"
    expected = ["developer"]
    assert parse(data) == expected
