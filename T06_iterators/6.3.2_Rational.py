class Rational:
    def __init__(self, n, d=0):
        try:
            assert isinstance(n, int) and isinstance(d, int) and d != 0
        except AssertionError:
            if d == 0 and type(n) == str:
                i = 0
                n_s = ''
                d_s = ''
                while True:
                    if n[i] != '/':
                        n_s += n[i]
                        i += 1
                    else:
                        i += 1
                        break
                while i < len(n):
                    d_s += n[i]
                    i += 1

                n, d = int(n_s), int(d_s)
            elif isinstance(n, float) or isinstance(d, float):
                raise ValueError('Parameters must be integer')
            elif d == 0:
                if isinstance(n, Rational):
                    pass
                else:
                    raise ZeroDivisionError('Division by zero is impossible')

        if isinstance(n, Rational):
            self.n = n.n
            self.d = n.d
        else:
            n_1, d_1 = abs(n), abs(d)
            if n_1 < d_1:
                n_1, d_1 = d_1, n_1
            while d_1 > 0:
                p = d_1
                d_1 = n_1 % d_1
                n_1 = p

            try:
                assert n_1 == 1
                self.n = n
                self.d = d
            except AssertionError:
                n /= n_1
                d /= n_1
                self.n = int(n)
                self.d = int(d)

        self._values = dict(n=self.n, d=self.d)

    def __add__(self, other):
        if isinstance(other, Rational):
            d = self.d * other.d
            n = self.n * other.d + other.n * self.d
            new = Rational(n, d)
            if new:
                return f'{n}/{d}'
        elif isinstance(other, float) or other == 0:
            raise ValueError("Wrong parameters")
        elif isinstance(other, int):
            d = self.d
            n = self.n + self.d * other
            new = Rational(n, d)
            if new:
                return f'{n}/{d}'

    def __sub__(self, other):
        if isinstance(other, Rational):
            d = self.d * other.d
            n = self.n * other.d - other.n * self.d
            new = Rational(n, d)
            if new:
                return f'{n}/{d}'
        elif isinstance(other, float) or other == 0:
            raise ValueError("Wrong parameters")
        elif isinstance(other, int):
            d = self.d
            n = self.n - self.d * other
            new = Rational(n, d)
            if new:
                return f'{n}/{d}'

    def __mul__(self, other):
        if isinstance(other, Rational):
            d = self.d * other.d
            n = self.n * other.n
            new = Rational(n, d)
            if new:
                return f'{n}/{d}'
        elif isinstance(other, float):
            raise ValueError("Wrong parameters")
        elif isinstance(other, int):
            d = self.d
            n = self.n * other
            new = Rational(n, d)
            if new:
                return f'{n}/{d}'

    def __truediv__(self, other):
        if isinstance(other, Rational):
            d = self.d * other.n
            n = self.n * other.d
            new = Rational(n, d)
            if new:
                return f'{n}/{d}'
        elif isinstance(other, float) and other == 0:
            raise ValueError("Wrong parameters")
        elif isinstance(other, int):
            d = self.d * other
            n = self.n
            new = Rational(n, d)
            if new:
                return f'{n}/{d}'

    def __call__(self):
        res = self.n / self.d
        return res

    def __getitem__(self, key):
        return str(self._values[key])


if __name__ == '__main__':
    r = Rational(2, 1)
    r2 = Rational(3, 4)
    r *= 4

    print(r2(), r2['d'])
