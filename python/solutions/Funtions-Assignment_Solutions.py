# Functions program

# Q1
# Write a Python function called `add_numbers` that takes two integers as parameters and returns their sum.
def add_numbers(num1, num2):
    sum = num1+num2
    return sum

num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
print(add_numbers(num1, num2))

# # Q2
# # Write a Python function called `greet` that prints "Hello, World!" when called.
userName = input("Enter your name:")
def greetings():
    print("Hi", userName, "how are you")
greetings()

# Q3
# write a Python function that takes two perameters: a number and an exponent(with a default value of 2). the function should return the result of raising the number to the given exponent.
def power(number, exponent=2):
    return number ** exponent

result = power(3)
print(result)

# Q4
# write a python function called 'average' that takes any number of arguments and return the average of those numbers
def average(num1, num2, num3, num4, num5):
    add = num1+num2+num3+num4+num5

    return add/5


result = average(2, 3, 4, 5, 6)
print(result)

# Q5
# Write a Python function called `create_person` that takes the parameters `name`, `age`, and `city` as keyword arguments and returns a dictionary representing a person with those attributes.
def create_person(name, age, city):
    person = {
        "name": name,
        "age": age,
        "city": city
    }
    return person
personName = input("Enter your name:")
personAge = input("Enteer your age:")
personCity = input("Enter your city:")
personDetail = create_person(personName, personAge, personCity)
print(personDetail)

# Q6
# Write a Python function called `factorial` that calculates the factorial of a given non-negative integer using recursion.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = 5
print("Factorial of", num, "is", factorial(num))

# Q7
# Write a Python function called `sum_list` that takes a list of integers as a parameter and returns the sum of all the elements in the list.
def sum_list(list):
    sum = 0
    for item in list:
        sum += item
    return sum
list_numbers = [20,30,40,10]
print(sum_list(list_numbers))

# Q8
# Write a Python function called `min_max` that takes a list of integers as a parameter and returns the minimum and maximum values in the list as a tuple.
def min_max(list1):
    return tuple(print("minimum number in list is",min(list1),"maximum number in list is",max(list1)))
list_numbers = [20,30,40,10]
min_max(list_numbers)

# Q9
# Write a Python function called `square_list` that takes a list of numbers as a parameter and returns a new list where each element is the square of the corresponding element in the input list, using a lambda expression.
def square_list(input_list):
    def square_func(x): return x ** 2
    squared_list = list(map(square_func, input_list))
    return squared_list

numbers = [1, 2, 3, 4, 5]
print("Squared list:", square_list(numbers))

# Q10
# Write a Python function named `calculate_area` that takes the radius of a circle as input and returns the area of the circle.
import math

def calculate_area(radius):
    area = math.pi * (radius ** 2)
    return area

radius = int(input("Enter radius of circle:"))
print("Area of the circle with radius", radius, "is:", calculate_area(radius))

# Q11
# Define a function called `is_even` that takes an integer as input and returns `True` if the number is even, otherwise `False`.
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

checkNum = int(input("Enter a number:"))
print(is_even(checkNum))

# Q12
# Create a function named `count_vowels` that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.
def count_vowels(input_string):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    for char in input_string:
        # Check if the character is a vowel
        if char.lower() in vowels:
            count += 1
    return count
text = input("Enter any text:")
print("Number of vowels in the text:", count_vowels(text))

# Q13
# Implement a function called `reverse_string` that takes a string as input and returns the reverse of the input string.
def reverse_string(any_string):
    print(any_string[::-1])
    return any_string
any_text = input("Enter a text:")
reverse_string(any_text)
    
# #Q14
# #Define a function called `find_max` that takes a list of numbers as input and returns the maximum value in the list.
def find_max(max_num):
    print("maximum number in the given list is:",max(max_num))
    return max_num
list_num = list(input("enter some numbers:"))
find_max(list_num)

#Q15
#Define a function called `merge_lists` that takes two lists as input and returns a new list containing all the elements from both input lists.
def merge_lists(list1,list2):
    new_list = list1 + list2
    print(new_list)
    return new_list
list3 = list(input("Enter list 1:"))
list4 = list(input("Enter list 2:"))
merge_lists(list3,list4)