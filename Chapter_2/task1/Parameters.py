class Parameters:
    def __init__(self, params):
        self.params = tuple(params)

    def __add__(self, other):
        if isinstance(other, Parameters):
            ps = Parameters([el1 + el2 for el1, el2 in zip(self.get_parameters(), other.get_parameters())])
        else:
            ps = Parameters(map(lambda p: p + other, self.params))
        return ps

    def __iadd__(self, other):
        if isinstance(other, Parameters):
            ps = Parameters([el1 + el2 for el1, el2 in zip(self.get_parameters(), other.get_parameters())])
        else:
            ps = Parameters(map(lambda p: p + other, self.params))
        return ps

    def __sub__(self, other):
        if isinstance(other, Parameters):
            ps = Parameters([el1 - el2 for el1, el2 in zip(self.get_parameters(), other.get_parameters())])
        else:
            ps = Parameters(map(lambda p: p - other, self.params))
        return ps

    def __isub__(self, other):
        if isinstance(other, Parameters):
            ps = Parameters([el1 - el2 for el1, el2 in zip(self.get_parameters(), other.get_parameters())])
        else:
            ps = Parameters(map(lambda p: p - other, self.params))
        return ps

    def __mul__(self, other):
        if isinstance(other, Parameters):
            ps = Parameters([el1 * el2 for el1, el2 in zip(self.get_parameters(), other.get_parameters())])
        else:
            ps = Parameters(map(lambda p: p * other, self.params))
        return ps

    def __imul__(self, other):
        if isinstance(other, Parameters):
            ps = Parameters([el1 * el2 for el1, el2 in zip(self.get_parameters(), other.get_parameters())])
        else:
            ps = Parameters(map(lambda p: p * other, self.params))
        return ps

    def __truediv__(self, other):
        if isinstance(other, Parameters):
            ps = Parameters([el1 / el2 for el1, el2 in zip(self.get_parameters(), other.get_parameters())])
        else:
            ps = Parameters(map(lambda p: p / other, self.params))
        return ps

    def __pow__(self, power, modulo=None):
        ps = Parameters(map(lambda p: p ** power, self.params))
        return ps

    def get_min(self):
        return min(self.get_parameters())

    def get_max(self):
        return max(self.get_parameters())

    def get_parameters(self):
        return tuple(self.params)

    def __str__(self):
        return self.get_parameters().__str__()