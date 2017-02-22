__author__ = 'PrasantJillella'
import module1
import random
'''Imports the module1 and uses the function average from it '''
x=random.randrange(1,100)
print("Hello we got ",x," as the random number from 1 to 100")
n=int(input("Enter the number of numbers to get their avg"))
lists=[]
print("Enter the",n ," numbers one by one")
for i in range(n):
    lists.append(int(input("Enter a number")))
print("The average of the numbers is :",module1.average(lists,n))
