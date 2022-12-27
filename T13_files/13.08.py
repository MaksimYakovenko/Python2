def print_poly(poly_koeffs):
    deg = len(poly_koeffs) - 1
    for k in poly_koeffs:
        if deg:
            print("{}x^{}".format(k, deg), end=" + ")
        else:
            print(k, end="\n")
        deg -= 1



def d_poly_koeffs(poly_koeffs):
    deg = len(poly_koeffs) - 1
    koeffs = []
    for i in range(deg):
        koeffs.append(deg * poly_koeffs[i])
        deg -= 1
    return koeffs


#Значення многочлена в т. x
def poly(x, poly_koeffs):
    n = len(poly_koeffs)
    deg = n - 1
    p = 0
    for i in range(n):
        xx = x ** deg
        p += poly_koeffs[i] * xx
        deg -= 1
    return p


poly_koeffs = [6, 2, 1]
print_poly(poly_koeffs)
print_poly(d_poly_koeffs(poly_koeffs))
print(poly(1, poly_koeffs))
