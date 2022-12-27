FILE = "input.txt"


def p(input):
    f = open(input, 'w')
    for i in range(0, 40):
        f.write(str(i) * 40 + "\n")
    f.close()


if name == 'main':
    p(FILE)
