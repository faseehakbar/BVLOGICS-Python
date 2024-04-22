# Q1 Set Creation and Manipulation Functions:

# - Write a function to create a set from user input.
def create_set():
    """This function takes user input for adding elements to a set."""
    my_set = set()
    for i in range(int(input("Enter the number of elements you want in your set (must be an integer): "))):
        element = input("Enter an element for your set:")
        my_set.update(element)
    return my_set


print(create_set(), "\n")

# element = input(f"Enter element {i+1}: ")
#     if element not in my_set:
#         my_set[element] = None
#     else:
#         print(f"Element '{element}' already exists in the set.")
# return set(my_set.keys())

# - Write a function to add an element to an existing set.


def add_element(existing_set, new_element):
    existing_set.add(new_element)


existing_set = {1, 2, 3}
new_element = int(input("Enter any integer element:"))
add_element(existing_set, new_element)
print("The updated set is :", existing_set, "\n")

# - Write a function to remove an element from a set.

def delete_element(a_set, elem):
    a_set.discard(elem)


a_set = {1, "two", 3.0, False}
print("Original set: ", a_set)
element = input("Enter an element you want to delete:")
delete_element(a_set, element)
print("Set after deletion: ", a_set, "\n")

# - Write a function to perform union of two sets.


def union_set(set1, set2):
    set3 = set1.union(set2)
    return set3


set1 = {1, 2, 3, "A"}
set2 = {"A", 2, "B", "C"}
print("Union of set1 and set2 is:", union_set(set1, set2), "\n")

# - Write a function to perform intersection of two sets.


def intersection_sets(set1, set2):
    result = set1.intersection(set2)
    return result


print("intersection of set1 and set2 is:", intersection_sets(set1, set2), "\n")

# - Write a function to perform difference between two sets.


def difference_set(set1, set2):
    diff = set1.difference(set2)
    return diff


print("Difference between set1 and set2 is", difference_set(set1, set2), "\n")

# - Write a function to perform symmetric difference between two sets.


def symm_diff(set1, set2):
    s_diff = set1.symmetric_difference(set2)
    return s_diff


print("Symmetric Difference Between set1 and set2 is :",
      symm_diff(set1, set2), "\n")

# Q2 Set Operations:
# - Write a function to check if a set is a subset of another set.


def is_subset(smaller, larger):
    return smaller.issubset(larger)


print("Is set1 a subset of  set2? ", is_subset(set1, set2), "\n")

# - Write a function to check if two sets are disjoint.
# A set is said to be disjoint with another set if it does not have any elements in common with the other set.


def disjoint_check(setA, setB):
    return setA.isdisjoint(setB)


print("Are set1 and set2 Disjoint ? ", disjoint_check(set1, set2), "\n")

# - Write a function to check if two sets are equal.
# (Note that this will also be True if they have different types, like one being a list and the other a tuple.)


def eq_check(setA, setB):
    return setA == setB


print("Are set1 and set2 Equal ? ", eq_check(set1, set2), "\n")

# - Write a function to find the length of a set.


def len_of_set(s):
    return len(s)


print("Length of set1 is :", len_of_set(set1), "\n")

# Q3 Set Membership Testing:
# - Write a function to test if an element exists in a set.

# This function, 'check_elem', takes in two parameters: 'element' and 'my_set'
# The purpose of this function is to check if the given 'element' is present in the 'my_set' set
# It returns a boolean value - True if the element is found in the set, False otherwise


def check_elem(element, my_set):
    # The 'in' keyword is used to check if the 'element' is present in the 'my_set'
    # If the element is found, the function returns True
    return element in my_set


print("Does 'a' exist in set1? ", check_elem('a', set1), "\n")

# - Write a function to test if all elements of a set satisfy a condition.

# This function, 'all_conditions', takes in one parameter: 'condition'
# The purpose of this function is to apply the provided 'condition' to each element of the 'my_set'.
# It should return True only if every element satisfies the condition, else it should return False.


def all_conditions(condition, my_set):
    for elem in my_set:
        if not condition(elem):  # If any element doesn't satisfy the condition, it returns false
            return False
    return True  # If all elements  satisfy the condition, it returns true


# Here we define a simple condition that checks whether an element is greater than 5 or not
def greater_than_five(x): return x > 5


print("Do all elements of set1  satisfy the condition (x>5)? ",
      all_conditions(greater_than_five, set1))

# Q4 Set Conversion:
#    - Write a function to convert a set to a list.


def set_to_list(st):
    return list(st)


print("\nList representation of set:", set1,
      "\n", "is", set_to_list(set1), "\n")

#    - Write a function to convert a list to a set.


def list_to_set(lst):
    return set(lst)


print("Set representation of list:", [
      "Hamza", 3, True], "\n", "is", list_to_set(["Hamza", 3, True]), "\n")
