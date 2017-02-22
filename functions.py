import math
__author__ = 'PrasantJillella'
def area_triangle(a=100,b=20,c=30):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
'''
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))'''
area=area_triangle(10,30)
print("The area is :",area)