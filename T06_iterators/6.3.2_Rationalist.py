from A_632_Rational import *


class Rationalist:
    def __init__(self):
        self._elements = []

    def __str__(self):
        return f'{self._elements}'

    def __setitem__(self, key, value):
        v = value
        if True:
            Rational(value)
        try:
            self._elements[key] = v
        except IndexError:
            self._elements.append(v)

    def __getitem__(self, key):
        try:
            return self._elements[key]
        except IndexError:
            return None

    def __len__(self):
        return len(self._elements)

    def __add__(self, other):
        if isinstance(other, Rationalist):
            res = Rationalist()
            count = 0
            for i in self._elements:
                res[self._elements.index(i)] = i
                count += 1
            for j in other._elements:
                res[count] = j
                count += 1
            return res
        elif isinstance(other, float):
            raise ValueError("Wrong parameters")
        elif isinstance(other, int):
            res = Rationalist()
            other = f'{other}/1'
            for i in self._elements:
                res[self._elements.index(i)] = i
            res[len(res)] = other
            return res
        elif True:
            Rational(other)
            res = Rationalist()
            for i in self._elements:
                res[self._elements.index(i)] = i
            res[len(res)] = other
            return res

    def __iadd__(self, other):
        if isinstance(other, Rationalist):
            count = len(self)
            for j in other._elements:
                self[count] = j
                count += 1
            return self._elements
        elif isinstance(other, float):
            raise ValueError("Wrong parameters")
        elif isinstance(other, int):
            other = f'{other}/1'
            self[len(self)] = other
            return self._elements
        elif True:
            Rational(other)
            self[len(self)] = other
            return self._elements

    def __iter__(self):
        return RationalistIncreasingIterator(*self._elements)


class RationalistIncreasingIterator:
    def __init__(self, *collection):
        self.values = list(collection)
        self.marker = 0
        n = len(self.values)

        for i in range(n - 1):
            for j in range(n - 1 - i):
                el1 = self.values[j]
                n_1 = ''
                d_1 = ''
                k1 = 0
                while True:
                    if el1[k1] != '/':
                        n_1 += el1[k1]
                        k1 += 1
                    else:
                        k1 += 1
                        break
                while k1 < len(el1):
                    d_1 += el1[k1]
                    k1 += 1
                el2 = self.values[j + 1]
                n_2 = ''
                d_2 = ''
                k2 = 0
                while True:
                    if el2[k2] != '/':
                        n_2 += el2[k2]
                        k2 += 1
                    else:
                        k2 += 1
                        break
                while k2 < len(el2):
                    d_2 += el2[k2]
                    k2 += 1
                n_1, n_2, d_1, d_2 = int(n_1), int(n_2), int(d_1), int(d_2)
                if d_1 < d_2:
                    self.values[j], self.values[j + 1] = self.values[j + 1], self.values[j]
                elif d_1 == d_2 and n_1 < n_2:
                    self.values[j], self.values[j + 1] = self.values[j + 1], self.values[j]

    def __next__(self):
        try:
            res = self.values[self.marker]
            self.marker += 1
            return res
        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    lst = Rationalist()
    lst[0] = "67/89"
    lst[21] = '21/2'
    lst[3] = '11/2'
    lst[21] = '2/21'
    for el in lst:
        print(el)




