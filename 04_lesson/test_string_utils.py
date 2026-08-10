import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('string, expected', [
    ("enjin", "Enjin"),
    ("my heart", "My heart")
    ])
def test_capitalize_positive(string, expected):
    assert utils.capitalize(string) == expected


@pytest.mark.negative
@pytest.mark.parametrize('string, expected', [
    ("", ""),
    (" ", " "),
    ("141", "141")
    ])
def test_capitalize_negative(string, expected):
    assert utils.capitalize(string) == expected


@pytest.mark.positive
@pytest.mark.parametrize('string, expected', [
    (" Simon", "Simon"),
    ("   Nanami", "Nanami"),
    (" 17", "17"),
    ("  Мне 2 булочки", "Мне 2 булочки")
    ])
def test_trim_positive(string, expected):
    assert utils.trim(string) == expected


@pytest.mark.negative
@pytest.mark.parametrize('string, expected', [
    ("", ""),
    (" ", "")
    ])
def test_trim_negative(string, expected):
    assert utils.trim(string) == expected


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, result', [
    ("Nasty", "t", True),
    ("Anastasia", "a", True),
    ("Yui", "K", False),
    ("221B", "1", True),
    ("Анна-Мария", "-", True),
    ("pupupu@mail.ru", "@mail.ru", True)
])
def test_contains_positive(string, symbol, result):
    assert utils.contains(string, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, result', [
    ("Yui", "R", False),
    ("TF 141", "Makarov", False)
])
def test_contains_negative(string, symbol, result):
    assert utils.contains(string, symbol) == result


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, expected', [
    ("Unlimited", "t", "Unlimied"),
    ("бара-бара-бара", "-", "барабарабара"),
    ("Entschu35ldigung", "35", "Entschuldigung")
])
def test_deleted_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, expected', [
    ("Toyota", "r", "Toyota"),
    ("кисуня", " ", "кисуня"),
    ("Kaffee", "", "Kaffee"),
    ("Tralalero Tralala", "67", "Tralalero Tralala")
])
def test_deleted_symbol_negative(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
