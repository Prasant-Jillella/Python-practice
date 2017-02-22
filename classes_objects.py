__author__ = 'PrasantJillella'
class Enemy:
    life=3
    def attack(self):
        self.life-=1
        print("ouch")
        if self.life<=0:
            print("I am Dead")
    def checklife(self):
        print(str(self.life)+" Health left")

enemy1=Enemy()
enemy1.attack()
enemy1.attack()
enemy1.attack()

enemy2=Enemy()
enemy2.attack()

enemy1.checklife()
enemy2.checklife()