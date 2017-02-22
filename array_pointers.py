__author__ = 'PrasantJillella'
def sum(lists):
    total=0
    for a in lists:
        total+= a
    return total
n=int(input("Enter the number of elements in the list"))
lists=[]
for i in range(n):
    lists.append(int(input("Enter the number")))
total=sum(lists)
print("The sum of the ",n," numbers is ", total)
