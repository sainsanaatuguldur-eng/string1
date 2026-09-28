import pytest
from assignment import (
    count_characters,
    remove_spaces,
    count_vowels,
    replace_vowels,
    count_words,
    find_longest_word,
)

# --- Exercise 1: Count characters ---
@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello world", 11),
        ("Python", 6),
        ("", 0),
        ("  spaced out  ", 14),
    ]
)
def test1(text, expected):
    assert count_characters(text) == expected


# --- Exercise 2: Remove spaces ---
@pytest.mark.parametrize(
    "text, expected",
    [
        ("Python is fun", "Pythonisfun"),
        ("   spaces   ", "spaces"),
        ("no_space", "no_space"),
        ("A B C D", "ABCD"),
    ]
)
def test2(text, expected):
    assert remove_spaces(text) == expected


# --- Exercise 3: Count vowels ---
@pytest.mark.parametrize(
    "text, expected",
    [
        ("Python is amazing", 5),
        ("HELLO WORLD", 3),
        ("sky", 0),
        ("aeiouAEIOU", 10),
    ]
)
def test3(text, expected):
    assert count_vowels(text) == expected


# --- Exercise 4: Replace vowels ---
@pytest.mark.parametrize(
    "text, expected",
    [
        ("Education", "*d*c*t**n"),
        ("HELLO", "H*LL*"),
        ("sky", "sky"),
        ("aeiou", "*****"),
    ]
)
def test4(text, expected):
    assert replace_vowels(text) == expected


# --- Exercise 5: Count words ---
@pytest.mark.parametrize(
    "text, expected",
    [
        ("Python makes coding fun", 4),
        ("One", 1),
        ("", 0),
        ("Two words", 2),
    ]
)
def test5(text, expected):
    assert count_words(text) == expected


# --- Exercise 6: Find longest word ---
@pytest.mark.parametrize(
    "text, expected",
    [
        ("Learning Python programming", "programming"),
        ("Short longest", "longest"),
        ("equal size", "equal"),
        ("", ""),
    ]
)
def test6(text, expected):
    assert find_longest_word(text) == expected
