class rovar:
    def __init__(self) -> None:
        # BUG FIX: Added missing 'g'
        self._LOWER_CONSTANTS = "bcdfghjklmnpqrstvwxz"
        # BUG FIX: Added missing 'D' and fixed the order
        self._UPPER_CONSTANTS = "BCDFGHJKLMNPQRSTVWXZ"

    def enrove(self, normal: str) -> str:
        '''Encode the string in rovarspraket.'''
        if normal is None:
            return None
        encoded = []
        for char in normal:
            if char in self._LOWER_CONSTANTS:
                encoded.append(char + 'o' + char)
            elif char in self._UPPER_CONSTANTS:
                # Standard Rover: Upper consonant + small 'o' + upper consonant
                encoded.append(char + 'o' + char)
            else:
                encoded.append(char)
        return ''.join(encoded)

    def derove(self, rov: str) -> str:
        '''Decode a string from rovarspraket.'''
        if rov is None:
            return None

        # Decoding lowercase
        for c in self._LOWER_CONSTANTS:
            find = c + 'o' + c
            rov = rov.replace(find, c)

        # BUG FIX: Changed 'O' to 'o' to match the enrove logic
        for c in self._UPPER_CONSTANTS:
            find = c + 'o' + c
            rov = rov.replace(find, c)

        return rov