import pytest
from ..src.parser import parse

'''
getList
get list with multiple words
get list of unique words
lowerCase
plural
synonyms

X "developer"				        —> ["developer"]
X None                              -> []
X ""                                  -> []
X "cool developer"		        —> ["cool", "developer"]
X "cool cool developer"		    —> ["cool", "developer"]

X "cool cool developer"		    —> !["developer","cool"]


X "DeveLoper"				        —> ["developer"]
X "developers"                    -> ["developer"]
X "coder"                         -> ["developer"]
X "coder programmer developer"    -> ["developer"]
X "coder programmers developers"  -> ["developer"]

"FinD all coders developer"     —> ["find", "all", "developer"]


'''


def test_parse_single_word():
    data = "developer"
    expected = ["developer"]
    assert parse(data) == expected


def test_null():
    data = None
    expected = []
    assert parse(data) == expected


def test_empty():
    data = ""
    expected = []
    assert parse(data) == expected


def test_parse_multiple_words():
    data = "cool developer"
    expected = ["cool", "developer"]
    assert parse(data) == expected


def test_parse_unique_words():
    data = "cool cool developer"
    expected = ["cool", "developer"]
    assert parse(data) == expected


def test_parse_unique_words_in_right_order():
    data = "cool cool developer"
    expected = ["developer", "cool"]
    assert parse(data) != expected


def test_case_sensitivity():
    data = "DeveLoper"
    expected = ["developer"]
    assert parse(data) == expected


def test_plural():
    data = "developers"
    expected = ["developer"]
    assert parse(data) == expected


def test_synonym():
    data = "coder"
    expected = ["developer"]
    assert parse(data) == expected


def test_multiple_synonyms():
    data = "coder programmer developer"
    expected = ["developer"]
    assert parse(data) == expected


def test_multiple_synonyms_with_plural():
    data = "coder programmers developers"
    expected = ["developer"]
    assert parse(data) == expected


def test_arbitrary_query():
    data = "FinD all coders developer"
    expected = ["find", "all", "developer"]
    assert parse(data) == expected
