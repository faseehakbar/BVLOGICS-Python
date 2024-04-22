#a = 30
#print(type(a))
#create a list of numbers and find the ssum of all numbers.

A = [23,22,21]
sum = 0
for item in A:
    sum += item
print(sum)

#given a list of strings, concatenate them into a singlestring
stringlist = ["Faseeh","akbar"]
singlestring = ""
for item in stringlist:
    singlestring += item
print(singlestring)

#find the maximum and minimum element in a list of numbers
print(min(A), max(A))


#check if a certain element exist in a list
list = [23,22,21]
print(30 in list)