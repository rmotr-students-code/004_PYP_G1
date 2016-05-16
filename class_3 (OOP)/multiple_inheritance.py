class Human(object):
    def walk(self):
        print("walk on two legs")


class Horse(object):
    def walk(self):
        print("walk on four legs")


class Centaur(Horse, Human):
    pass


c = Centaur()
print(Centaur.__mro__)