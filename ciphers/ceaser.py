class Ceaser:

    def __init__(self, alphabet, shift):
        if isinstance(alphabet, str):
            alphabet = list(alphabet)
        self.alphabet = alphabet
        self.shift = shift

    def encode(self, val):

        if isinstance(val, str):
            val = list(val)

        if not self._is_valid_input(val):
            raise ValueError('Your input value does not match the alphabet')

        for i in range(0, len(val)):
            val[i] = self.alphabet[self._compute_encode_shift_index(val[i])]

        return val

    def decode(self, val):

        if isinstance(val, str):
            val = list(val)

        if not self._is_valid_input(val):
            raise ValueError('Your input value does not match the alphabet')

        for i in range(0, len(val)):
            val[i] = self.alphabet[self._compute_decode_shift_index(val[i])]

        return val


    def _is_valid_input(self, val):

        if isinstance(val, str):
            val = list(val)

        for v in val:
            if not v in self.alphabet:
                return False

        return True

    def _compute_encode_shift_index(self, val):
        base = self.alphabet.index(val)
        return (base + self.shift) % len(self.alphabet)

    def _compute_decode_shift_index(self, val):
        base = self.alphabet.index(val)
        return (base - self.shift) % len(self.alphabet)
