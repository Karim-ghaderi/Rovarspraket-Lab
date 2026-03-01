class Rover:
    _LOWER_CONSTANTS = "bcdfghjklmnpqrstvwxz"
    _UPPER_CONSTANTS = "BCDFGHJKLMNPQRSTVWXZ"

    def enrove(self, text:str)->str:
        if text is None: return None
        encoded = []
        for char in text:
            if char in self._LOWER_CONSTANTS:
                encoded.append(char + 'o' + char)
            elif char in self._UPPER_CONSTANTS:
                encoded.append(char + 'o' + char)
            else:
                encoded.append(char)
        return ''.join(encoded)

    def derove(self, rov:str)->str:
        if rov is None: return None
        for c in self._LOWER_CONSTANTS:
            find = c+'o'+c
            rov = rov.replace(find, c)
        for c in self._UPPER_CONSTANTS:
            find = c+'O'+c # باگ اینجاست (O بزرگ به جای o کوچک)
            rov = rov.replace(find, c)
        return rov