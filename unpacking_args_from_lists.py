__author__ = 'PrasantJillella'
def average(arg1,arg2,arg3):
    avg=(arg1+arg2+arg3)/3
    return avg
list=[]
for i in range(3):
    list.append(int(input("enter element into list")))
print("The average of 3 numbers is ",average(*list))
print("The avergae of 3 numbers is ",average(list[0],list[1],list[2]))
'''These both statements are one and the same but the first one is much more easy to implement '''