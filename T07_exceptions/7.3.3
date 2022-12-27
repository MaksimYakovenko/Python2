from 7.3.1 import RationalError
from 7.3.2 import RationalValueError


class Rational:
    def __init__(self, n, d=0):
        try:
            assert isinstance(n, int) and isinstance(d, int) and d != 0
        except AssertionError:
            if d == 0 and type(n) == str:
                i = 0
                n_s = ''
                d_s = ''
                try:
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
                except IndexError:
                    raise RationalValueError(RationalValueError.WrongValue, f"{n}")

                try:
                    n, d = int(n_s), int(d_s)
                except ValueError:
                    raise RationalValueError(RationalValueError.WrongValue, f"{n_s}/{d_s}")
                except TypeError:
                    raise RationalValueError(RationalValueError.WrongValue, f"{n}")

                if d == 0:
                    raise RationalError(RationalError.DivbyZero, f"{n}/{d}")
            elif isinstance(n, float) or isinstance(d, float):
                raise RationalValueError(RationalValueError.WrongValue, f"{n}/{d}")
            elif d == 0:
                if isinstance(n, Rational):
                    pass
                else:
                    raise RationalError(RationalError.DivbyZero, f"{n}/{d}")

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
            if self.n == 0:
                new = other
                return new
            else:
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
            if other == 0:
                n = 0
                d = 1
                Rational(n, d)
                return f'{n}/{d}'
            else:
                d = self.d
                n = self.n * other
                Rational(n, d)
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
    r1 = Rational(9, 2)
    try:
        r2 = Rational(3, 0)
    except RationalError as myError:
        if myError.errorCode == RationalError.DivbyZero:
            print("Відбулося ділення на нуль")
            print(myError)

