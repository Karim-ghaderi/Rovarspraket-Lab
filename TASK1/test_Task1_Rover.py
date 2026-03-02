'''
Student shall write their names here
1. [Student Name 1]
2. [Student Name 2]
'''

import pytest
from Task1_Rover import rovar

class TestString:
    '''
    Test cases for Rövarspråket using Pytest.
    Targeting 100% statement and branch coverage.
    '''

    @pytest.fixture(autouse=True)
    def setup(self):
        '''Set up shared resources: Class instance to access rover methods'''
        self.rv = rovar()

    # --- Test Cases for enrove ---

    def test_enrove_null(self):
        '''Test enrove with Null input'''
        assert self.rv.enrove(None) is None

    def test_enrove_empty(self):
        '''Test enrove with an empty string'''
        assert self.rv.enrove("") == ""

    def test_enrove_lowercase_consonants(self):
        '''Test all lowercase consonants including 'g' (Fixes original bug)'''
        input_str = "bcdfghjklmnpqrstvwxz"
        expected = "bobcocdodfofgoghohjojkoklolmomnonpopqoqrorsostotvovwowxoxzoz"
        assert self.rv.enrove(input_str) == expected

    def test_enrove_uppercase_consonants(self):
        '''Test all uppercase consonants including 'D' (Fixes original bug)'''
        input_str = "BCDFGHJKLMNPQRSTVWXZ"
        expected = "BoBCoCDoDFoFGoGHoHJoJKoKLoLMoMNoNPoPQoQRoRSoSToTVoVWoWXoXZoZ"
        assert self.rv.enrove(input_str) == expected

    def test_enrove_vowels_swedish(self):
        '''Test Swedish and English vowels remain unchanged'''
        vowels = "aeiouyåäöAEIOUYÅÄÖ"
        assert self.rv.enrove(vowels) == vowels

    # --- Test Cases for derove ---

    def test_derove_null(self):
        '''Test derove with Null input'''
        assert self.rv.derove(None) is None

    def test_derove_empty(self):
        '''Test derove with an empty string'''
        assert self.rv.derove("") == ""

    def test_derove_logic_mismatch_fix(self):
        '''Test if decoder handles uppercase correctly (Fixes the 'O' vs 'o' bug)'''
        assert self.rv.derove("BoB") == "B"

    def test_numbers_and_punctuation(self):
        '''Test that numbers and symbols are ignored'''
        data = "123 !#."
        assert self.rv.enrove(data) == data
        assert self.rv.derove(data) == data

if __name__ == '__main__':
    pytest.main(["-v"])