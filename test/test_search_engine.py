import pytest

'''
getList
get list with multiple words
get list of unique words
lowerCase
plural
synonyms

Null -> []
"" -> []
"developer"				        —> ["developer"]
"cool developer"		        —> ["cool", "developer"]
"cool cool developer"		    —> ["cool", "developer"]
"DeveLoper"				        —> ["developer"]
"developers"                    -> ["developer"]
"coder"                         -> ["developer"]
"coder programmer developer"    -> ["developer"]
"coder programmers developers"  -> ["developer"]

"FinD all coders developer"     —> ["find", "all", "developer"]






'''


def test_search_engine():
    assert True
