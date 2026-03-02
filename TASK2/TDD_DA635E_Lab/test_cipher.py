#install pytest-cov. (pip install pytest-cov)
#Run tests with coverage: run tests and generate HTML (pytest --cov=.) (--cov-report=html) (--cov-branch)
#--cov=. specifies the directory to measure coverage for (current directory in this case)
#--cov-report=html : generates html report
#--cov-branch includes branch coverage in the report. 

import pytest
from cipher import cipher_function

def test_empty_string():
    assert cipher_function("") == ""


def test_none_input():
    assert cipher_function(None) is None


def test_numbers():
    assert cipher_function("123") == "123"


def test_special_characters():
    assert cipher_function("!@#") == "!@#"


def test_single_letter():
    assert cipher_function("a") == "a"


def test_two_letter_palindrome():
    assert cipher_function("aa") == "aa"


def test_palindrome():
    assert cipher_function("level") == "level"


def test_repeated_letters():
    assert cipher_function("hello") == "olleh"


def test_unique_letters():
    assert cipher_function("cat") == "atc"


def test_conflict_palindrome_priority():
    assert cipher_function("noon") == "noon"


def test_case_insensitive_palindrome():
    assert cipher_function("Level") == "Level"


def test_unique_letters_with_uppercase():
    assert cipher_function("Python") == "ythonP"