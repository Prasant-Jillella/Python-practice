__author__ = 'PrasantJillella'
class mashroom:
    def eat_mashroom(self):
        print("I am going big")
class jump:
    def jumps(self):
        print("i am jumping")
class mario(mashroom, jump):
    pass

mario1=mario()

mario1.eat_mashroom()

mario1.jumps()