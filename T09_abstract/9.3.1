from random import randint
from abc import ABCMeta , abstractmethod

class Student(metaclass=ABCMeta):
    def __init__(self):
        self._scholarship = 0
        self._helps = 0
        self._hostel = 0
        self._canteen = 0
        self._f = open(f_name, "r", encoding="UTF-8")
        self._c = self._f.readlines()
        self._kredits = int(*self._c[1].split())
        self._money = int(*self._c[2].split())
        self._li = ' '

    @abstractmethod
    def accept(self , visitor):
        pass

class NaturalHumanitarian(Student):
    def __init__(self ):
        super().__init__()
        self._humanitarian = 0
        self._teach_natural = 0

    def accept(self , visitor):
        visitor.visit(self)

    def WorkWithNaturalHumanitarianFile(self):
        self._hostel = 0
        self._scholarship = 0
        self._helps = 0
        self._canteen = 0

        self._f = open(f_name, "r", encoding="UTF-8")
        self._c = self._f.readlines()
        for j in self._c:
            self._li = j.split()
            try:
                if self._li[1] == "humanitarian":
                    self._scholarship += int(self._li[2])
                elif self._li[1] == "scholarship":
                    self._scholarship += int(self._li[2])
                elif self._li[1] == "help":
                    self._helps += int(self._li[2])
                elif self._li[1] == "hostel":
                    self._hostel += int(self._li[2])
                elif self._li[1] == "canteen":
                    self._canteen += int(self._li[2])
                elif self._li[1] == "natural":
                    self._teach_natural += int(self._li[2])
            except IndexError:
                continue

    def __str__(self):
        return (f"Чи оплатив студент всі борги:{str(self._money >= (self._hostel + self._canteen - self._helps) )} \n"
                f"Чи набрав студент достатню к-сть кредитів:{str(self._kredits >= self._teach_natural + self._humanitarian)} ")

class Natural(Student):
    def __init__(self):
        super().__init__()
        self._teach_natural = 0

    def accept(self, visitor):
        visitor.visit(self)

    def WorkWithNaturalFile(self):
        self._hostel = 0
        self._scholarship = 0
        self._helps = 0
        self._canteen = 0

        self._f = open(f_name, "r", encoding="UTF-8")
        self._c = f.readlines()
        for j in self._c:
            li = j.split()
            try:
                if li[1] == "natural":
                    self._teach_natural += int(li[2])
                elif li[1] == "scholarship":
                    self._scholarship += int(li[2])
                elif li[1] == "help":
                    self._helps += int(li[2])
                elif li[1] == "hostel":
                    self._hostel += int(li[2])
                elif li[1] == "canteen":
                    self._canteen += int(li[2])
            except IndexError:
                continue

    def __str__(self):
        return (f"Чи оплатив студент всі борги:{str(self._money >= (self._hostel + self._canteen - self._helps))} \n"
                f"Чи набрав студент достатню к-сть кредитів:{str(self._kredits >= self._teach_natural )} ")


class Humanitarian(Student):
    def __init__(self):
        super().__init__()
        self._humanitarian = 0

    def accept(self, visitor):
        visitor.visit(self)

    def WorkWithHumanitarianFile(self):
        self._hostel = 0
        self._scholarship = 0
        self._helps = 0
        self._canteen = 0

        self._f = open(f_name, "r", encoding="UTF-8")
        self._c = f.readlines()
        for j in self._c:
            li = j.split()
            try:
                if li[1] == "humanitarian":
                    self._humanitarian  += int(li[2])
                elif li[1] == "scholarship":
                    self._scholarship += int(li[2])
                elif li[1] == "help":
                    self._helps += int(li[2])
                elif li[1] == "hostel":
                    self._hostel += int(li[2])
                elif li[1] == "canteen":
                    self._canteen += int(li[2])
            except IndexError:
                continue

    def __str__(self):
        return (f"Чи оплатив студент всі борги:{str(self._money >= (self._hostel + self._canteen - self._helps))} \n"
                f"Чи набрав студент достатню к-сть кредитів:{str(self._kredits >=  self._humanitarian)} ")

class Visitor(metaclass=ABCMeta):

    @abstractmethod
    def visit(self , student):
        pass


class visitNaturalHumanitarian(Visitor):

    def visit(self , student):
        student.WorkWithNaturalHumanitarianFile()

    def __str__(self):
        return str("i visit NaturalHumanitarian" )

class visitHumanitarian(Visitor):

    def visit(self, student):
        student.WorkWithHumanitarianFile()

    def __str__(self):
        return str("i visit Humanitarian" )

class visitNatural(Visitor):

    def visit(self, student):
        student.WorkWithNaturalFile()

    def __str__(self):
        return str("i visit Natural" )



N_MAXKEY = 25
MULT = 4

ACTIONS = [
    "teach humanitarian",  # вивчити гуманітарну дисципліну
    "teach natural",  # вивчити природничу дисципліну
    "obtain scholarship",  # отримати стипендію
    "obtain help",  # отримати допомогу від батьків
    "pay hostel",  # заплатити за гуртожиток
    "pay canteen",  # заплатити за харчування у столовій
]

DIRECTIONS = [
    "humanitarian",  # гуманітарни напрям
    "natural",  # природничий напрям
    "natural-humanitarian",  # природничо-гуманітарний напрям
]

def generate( fname, actions_number):
    ACTIONS_COUNT = len(ACTIONS)
    DIRECTIONS_COUNT = len(DIRECTIONS)

    with open(fname, "w", encoding='utf-8') as f_out:
        direction = DIRECTIONS[randint(0, DIRECTIONS_COUNT - 1)]
        print("%30s" % direction, file=f_out)
        credit_count = randint(200, 600)
        print("%30s" % credit_count, file=f_out)
        start_money = randint(2000, 60000)
        print("%30s" % start_money, file=f_out)

        for i in range(actions_number):

            action = ACTIONS[randint(0, ACTIONS_COUNT - 1)]
            print("%30s" % action, file=f_out, end=" ")
            if action == "teach humanitarian":
                action_prop = randint(1, 10)
                print("%5s" % action_prop, file=f_out, end=" ")
            elif action == "teach natural":
                action_prop = randint(1, 10)
                print("%5s" % action_prop, file=f_out, end=" ")
            elif action == "obtain scholarship":
                action_prop = 1500
                print("%5s" % action_prop, file=f_out, end=" ")
            elif action == "obtain help":
                action_prop = randint(1, 10) * 100
                print("%5s" % action_prop, file=f_out, end=" ")
            elif action == "pay hostel":
                action_prop = 300
                print("%5s" % action_prop, file=f_out, end=" ")
            elif action == "pay canteen":
                action_prop = randint(50, 100)
                print("%5s" % action_prop, file=f_out, end=" ")

            print(file=f_out)



if __name__ == "__main__":

    for j in range(1, 15):
        d = "" if j >= 10 else "0"
        f_name = "input" + d + str(j) + ".txt"
        generate(f_name, 500)
        f = open(f_name, "r", encoding="UTF-8")
        c = f.readlines()

        nh = NaturalHumanitarian()
        h = Humanitarian()
        n = Natural()
        if "natural-humanitarian" in c[0]:
            vis = [visitNaturalHumanitarian()]
            for i in vis:
                print("Студент номер " , j)
                print(i)
                nh.accept(i)
                print(nh)
            print()

        elif "humanitarian" in c[0]:
            vis = [ visitHumanitarian()]
            for i in vis:
                print("Студент номер ", j)
                print(i)
                h.accept(i)
                print(h)
            print()

        elif "natural" in c[0]:
            vis = [visitNatural()]
            for i in vis:
                print("Студент номер ", j)
                print(i)
                n.accept(i)
                print(n)
            print()
