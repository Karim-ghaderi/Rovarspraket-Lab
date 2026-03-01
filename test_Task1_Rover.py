import pytest
from Task1_Rover import Rover

def test_vowels():
    r = Rover()
    assert r.enrove("a") == "a"

def test_consonants():
    r = Rover()
    assert r.enrove("b") == "bob"

def test_uppercase_bug():
    r = Rover()
    # این تست نشان می‌دهد که Decoder حروف بزرگ را درست برنمی‌گرداند
    assert r.derove("BoB") == "B"