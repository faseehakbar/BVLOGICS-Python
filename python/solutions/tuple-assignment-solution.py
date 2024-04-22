# -=-=-=-=21-03-2024-=-=-=-==-=
# TUPLE ASSIGNMENT

# Q1Tuple Manipulation:
# - Write a function to create a tuple from user input.
def  create_tuple():
    tup = []
    for i in range(7):
        tup.append(input("enter any thing which you want in your tuple:"))
    return tup

print(tuple(create_tuple()))

# # - Write a function to add an element to an existing tuple and return the new tuple.
def add_element(t, e):
    t += (e,)
    return t


T = ("Hamza", "raza", "Ali")
E = input("Enter anything that you want to add into the tuple :")
print(add_element(T, E))

# - Write a function to remove an element from a tuple and return the new tuple.
# T = ("Ali",2,False,"Sara","Hamza",5,True)
# def delete_element(t,i):
#         if len(t) <= i:
#             print("Invalid index")
#         else:
#             t = t[:i] + t[i+1:]
#             return t
# I = int(input("Enter the position of the element that you want to delete: "))
# print(delete_element(T, I))

# - Write a function to concatenate two tuples and return the result.
# def concat_tuples(a, b):
#     return a + b


# A = (1, 2, 3, 4, 5)
# B = ('a', 'b', 'c')
# C = concat_tuples(A, B)
# print(C)

# # - Write a function to find the length of a tuple.

# def tuple_length(tup):
#     return len(tup)
# Tuple = (1, "Faseeh", True, 9.9)
# print(tuple_length(Tuple))

# @2Tuple Operations:
# - Write a function to find the maximum and minimum elements of a tuple.
def max_min_elements(tup):
    return print("The maximum value is:", max(tup), "\n The minimum value is:", min(tup))


tuple_data = (8, 67, 45, 23, 90, 12)
max_min_elements(tuple_data)

# - Write a function to check if an element exists in a tuple.


def check_element(fruits, item):
    return item in fruits


fruits = ("Apple", "Orange", "Cherry", "Grapes")
print("Checking element \"Cherry\" in tuple ",
      fruits, " -> ", check_element(fruits, "Cherry"))
print("")

# - Write a function to count the occurrences of an element in a tuple.
my_integers = (1, 2, 5, 7, 9, 2, 3, 7, 11)


def count_items(my_integers, item):
    return my_integers.count(item)


print("Counting how many times item 7 exist in tuple ",
      my_integers, " -> ", count_items(my_integers, 7))
print("")

# - Write a function to reverse a tuple.


def reverse_tuple(fruits):
    return fruits[::-1]


print("Reversing fruits tuple ", fruits, " -> ", reverse_tuple(fruits))
print("")

# - Write a function to sort a tuple.


def sort_tuple(my_integers):
    return tuple(sorted(my_integers))


print("Sorting integers tuple ", my_integers, " -> ", sort_tuple(my_integers))
print("")

# Q3Tuple Unpaking
# - Write a function to unpack a tuple into individual variables.
print("")


def unpack_tuple(my_tuple):
    var1, var2, var3 = my_tuple
    return var1, var2, var3


my_tuple = (1, 2, 3)
var1, var2, var3 = unpack_tuple(my_tuple)
print("Unpacked variables from ", my_tuple, " are ", var1, var2, var3)
print("")

# - Write a function to zip two tuples and return a list of tuples.
fruits = ("Apple", "Orange", "Cherry", "Grapes")
cars = ("Volvo", "BMW", "Toyota")


def zip_tuples(tuple1, tuple2):
    return list(zip(tuple1, tuple2))


print("Zip two tuples ", fruits, ", ", cars,
      " and return list of tuples ", zip_tuples(fruits, cars))
print("")

# Q4Tuple Slicing
# - Write a function to slice a tuple based on start and end indices.
print("")
my_integers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)


def slice_tuple(tuple1):
    return tuple1[2:7]


print("Slicing tuple ", my_integers,
      " from indices 2 to 7 ", slice_tuple(my_integers))
print("")

# - Write a function to return the first n elements of a tuple.


def slice_n_items(tuple1, n):
    return tuple1[:n]


print("Slicing first 5 elements of tuple ", my_integers,
      " -> ", slice_n_items(my_integers, 5))
print("")

# Q5Tuple Iteration
# - Write a function to iterate over a tuple and print its elements.
print("")
fruits = ("Apple", "Orange", "Cherry", "Grapes")


def iterate_tuple(my_tuple):
    for i in my_tuple:
        print(i)


print("Iterating fruits tuple ", fruits)
iterate_tuple(fruits)
print("")

# - Write a function to find the index of a specific element in a tuple.


def find_index(my_tuple, item):
    return my_tuple.index(item)


print("Finding the index of \"Cherry\" in tuple ",
      fruits, " -> ", find_index(fruits, "Cherry"))
print("")

# Q6Tuple Paking_unpaking
# - Write a function to pack and return multiple values as a tuple.
print("")


def pack_values(*args):
    return args


print(
    "Packed multiple values as a tuple 10, \"hello\", [1, 2, 3] ", " -> ", pack_values(10, "hello", [1, 2, 3]))
print("")

# - Write a function to unpack a tuple returned by another function.


def unpack_tuple():
    return pack_values(10, "hello", [1, 2, 3])


print("Unpacked multiple values from a tuple ", pack_values(
    10, "hello", [1, 2, 3]), " -> ", *unpack_tuple())
print("")

# Q7
# - Write a function to test if a given tuple is a subset of another tuple.
print("")
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3, 4, 5)


def is_subset(subset, superset):
    return set(subset).issubset(set(superset))


print("Is ", tuple1, " a subset of ", tuple2, " ? ", is_subset(tuple1, tuple2))
print("")

# - Write a function to test if all elements of a tuple satisfy a condition.


def all_elements_satisfy_condition(t, condition):
    for element in t:
        if not condition(element):
            return False
    return True


tuple3 = (1, 2, 3, 4, 5)
print("Do all elements of ", tuple3, " satisfy the condition (even)? ",
      all_elements_satisfy_condition(tuple3, lambda x: x % 2 == 0))
print("")

# Q8
# - Write a function to convert a tuple to a list.
print("")
cars_tuple = ("Volvo", "BMW", "Toyota")


def tuple_to_list(my_tuple):
    return list(my_tuple)


print("Converting cars tuple ", cars_tuple,
      " to list ", tuple_to_list(cars_tuple))
print("")

# - Write a function to convert a list to a tuple.
cars_list = ["Volvo", "BMW", "Toyota"]


def list_to_tuple(my_list):
    return tuple(my_list)


print("Converting cars list ", cars_list,
      " to tuple ", list_to_tuple(cars_list))
print("")
