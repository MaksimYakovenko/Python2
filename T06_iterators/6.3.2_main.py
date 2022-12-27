from A_632_Rationalist import *


if __name__ == '__main__':

    elem = []

    with open("input02.txt") as f:
        for line in f:
            start_el = [el for el in line.split()]
            for x in start_el:
                if x.find('/') == -1:
                    int(x)
                    start_el[start_el.index(x)] = f'{x}/1'
            elem.append(start_el)

    for i in elem:
        lst = Rationalist()
        count = 0
        for j in i:
            lst[count] = j
            count += 1
        print('************************************')
        for pos in lst:
            print(pos)

