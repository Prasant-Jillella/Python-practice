__author__ = 'PrasantJillella'
def check(sets,a):
    if a in sets:
        print("you already have",a,"in the set")
    else:
        print(a,"has been added to the set")
        sets.add(a)
'''Sets cannot be appended we can use add function in it though'''
sets={"prasant","Santosh","daya"}
check(sets,"prasant")
check(sets,"Satyavani")
'''check(sets,"daya")'''
print("The set is",sets)