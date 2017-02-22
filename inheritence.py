__author__ = 'PrasantJillella'
class parent:

    def last_name(self):
        print("Jillella")

class child(parent):
    def first_name(self):
        print("Prasant")
    '''def last_name(self):print("jill")'''
name=parent()
name.last_name()

name1=child()
name1.first_name()
name1.last_name()