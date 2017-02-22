__author__ = 'PrasantJillella'
class Enemy:
    name="prasant's game"   '''this is a class variable'''
    def __init__(self,y=10):
        self.energy=y '''instance variable og the class'''
    def energy_disp(self):
        print(self.energy)

Krish=Enemy(10)
Prasant=Enemy(100)

Krish.energy_disp()
Prasant.energy_disp()
