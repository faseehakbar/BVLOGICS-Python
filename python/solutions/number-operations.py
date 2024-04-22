#find the square root of a given number(use a built-in function)
import math

mynumbner = 23
print(math.sqrt(mynumbner))

#check if the number is prime
if(mynumbner % 2 == 0):
    print("yes")
else:
    print("no")

#generate a list of prime numbers within a given range of 99
mylist = []

i = 0
while i<=99:
    if(i % 2 ==0):
        mylist.append(i)
    i += 1
print(mylist)

#calculate the factorial of a number
print(math.factorial(12))
