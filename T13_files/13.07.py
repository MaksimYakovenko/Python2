def a(filename):
    f = open(filename)
    for line in f:
        new = line.split()
        max_length = 0
        max_word = ""

        for word in new:
            if len(word) > max_length:
                max_length = len(word)
                max_word = word

        print(max_word)



def b(filename):
    f = open(filename)
    s = input().split()
    print(len(s))
