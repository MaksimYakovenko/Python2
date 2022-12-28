try:
    f = open("content.txt")
except FileNotFoundError as e:
    print("Файл content.txt не існує за вказаним розташуванням:", e)
except PermissionError as e:
    print("Файл content.txt не доступний для читання:", e)
else:
    for line in f:
        try:
            g = open("{}".format(line.rstrip()))
        except FileNotFoundError as e:
            print("Файл {} не існує за вказаним розташуванням:".format(line), e)
        except PermissionError as e:
            print("Файл {} не доступний для читання:".format(line), e)
        else:
            try:
                content = g.read()
            except TypeError as e:
                print("Файл content.txt містить не лише дійснi числа:", e)
            else:
                print(content)
                f.close
