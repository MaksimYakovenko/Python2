class Figure:

    def dim(self):
        pass

    def perimeter(self):
        try:
            assert (self.dim() == 2)
        except AssertionError:
            return None

    def square(self):
        try:
            assert (self.dim() == 2)
        except AssertionError:
            return None

    def squareSurface(self):
        try:
            assert(self.dim() == 3)
        except AssertionError:
            return None

    def squareBase(self):
        try:
            assert (self.dim() == 3)
        except AssertionError:
            return None

    def height(self):
        try:
            assert (self.dim() == 3)
        except AssertionError:
            return None

    def _volume(self):
        if self.dim() == 2:
            S = self.square()
            try:
                return float(S)
            except TypeError:
                S = 0
                return S

        else:
            return self._volume()

    def show(self):
        print(f"{self.__class__}: dimention = {self.dim()}, volume = {self._volume()}")


if __name__ == '__main__':
    eq = Figure()
    print(eq)
