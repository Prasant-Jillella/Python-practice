__author__ = 'PrasantJillella'
def sum(*lists):
    total=0
    for a in lists:
        total+= a
    return total
print("The sum of 4 elements is ",sum(10,20,30,40))
print("The sum of 5 elements is ",sum(10,20,30,40,50))
