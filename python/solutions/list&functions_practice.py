# Lists with Functions
# 13-March-2024(Wednesday)

# Q1
# Create a function that takes a list of numbers as input
# and returns the sum of all the numbers.
list = []
for i in range(5):
    list.append(int(input("Entar a number:")))

def sumListItems(input_list):
    sum = 0
    for item in input_list:
        sum += item
    return sum
print(sumListItems(list))

# Q2
# Write a function that takes two lists as input and returns a new list containing elements that are common to both input lists.
list1 = []
list2 = []
for i in range(5):
    list1.append(input("Entar a number:"))
for i in range(5):
    list2.append(input("Entar a number:"))
def common_element(list1,list2):
    return list(set(list1).intersection(set(list2)))
print(common_element(list1,list2))

# Q3
# Implement a function that takes a list of strings as
# input and returns the longest string in the list.
def longest_string(strings):
    if not strings:
        return None  # Return None if the list is empty

    longest = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest):
            longest = string
    return longest
stringList = []
for i in range(5):
    stringList.append(input("Entar a string:"))

print(longest_string(stringList))

# Q4
# Create a function that takes a list of integers as input
# and returns a new list with only the even numbers
# from the input list.
intList = []
for i in range(5):
    intList.append(int(input("Entar a number:")))

def even_number(input_list):
    even_list = []
    for i in input_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list
print(even_number(intList))

# Q5
# Write a function that takes a list of strings as input and
# returns a new list with the strings sorted
# alphabetically.
string_list = []
for i in range(5):
    string_list.append(input("Entar a string:"))

def sorted_string(input_string_list):
    return sorted(input_string_list)

print(sorted_string(string_list))

# Q6
# Implement a function that takes a list of numbers as
# input and returns the average of all the numbers in the
# list.
number_list = []
for i in range(5):
    number_list.append(int(input("Entar a number:")))

def average_numnber(input_list):
    sum = 0
    for i in input_list:
        sum += i
    return sum/5
print(average_numnber(number_list))

# Q7
# Create a function that takes a list of numbers as input
# and returns a new list with the square of each number
# in the input list.
number_list = []
for i in range(5):
    number_list.append(int(input("Entar a number:")))
    
def square_list_numberes(input_list):
    squared_list = []
    for num in input_list:
        squared_list.append(num ** 2)
    return squared_list
print(square_list_numberes(number_list))

# Q8
# Write a function that takes a list of strings as input and
# returns a new list with the length of each string in the
# input list.
input_string_list = []
for i in range(5):
    input_string_list.append(input("Entar a string:"))
def str_length(input_list):
    item_length = []
    for i in input_list:
        item_length.append(len(i))
    return item_length
print(str_length(input_string_list))

#Q9
# Implement a function that takes a list of integers as
# input and returns the largest number in the list.
int_list = []
for i in range(5):
     int_list.append(int(input("Entar a number:")))
def largest_number(input_list):
    return max(input_list)
print(largest_number(int_list))

# Q10
# Create a function that takes two lists of equal
# length as input and returns a new list where each
# element is the sum of the corresponding elements
# from the input lists.

int_list1 = []
int_list2 = []
for i in range(5):
     int_list1.append(int(input("Entar a number:")))
for i in range(5):
     int_list2.append(int(input("Entar a number:")))
     
def add_corresponding_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Input lists must have equal length")

    return [x + y for x, y in zip(list1, list2)]
print(add_corresponding_elements(int_list1,int_list2))