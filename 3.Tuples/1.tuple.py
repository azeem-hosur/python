# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets*.

my_tuple = ("apple","banana","orange")
print(my_tuple)

# *Tuples can also be created without the parentheses:
t1 = "apple","banana","orange"
print(t1)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:
t2 = ("apple","banana","grapes","mango","apple")
print(t2)

# Tuple Length
# To determine how many items a tuple has, use the len() function:
print(len(t2))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
t3 = ("apple")  # <class 'str'>
print(type(t3))

t4 = ("apple",) # <class 'tuple'>
print(type(t4))

# Create an Empty Tuple
# To create an empty tuple, use round brackets with no content.
t5 = ()
print(type(t5))

# Tuple Items - Data Types
# Tuple items can be of any data type:
tu1 = ("apple","banana","grapes","mango")
tu2 = (1,2,3,4,5)
tu3 = (True, False, True, False)

print(f"{tu1}, {tu2}, {tu3}")

# A tuple can contain different data types:
tu4 = ("abc", 1,2,3, True)
print(tu4)

# type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple':

# <class 'tuple'>
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
tup1 = tuple(("apple","mango"))
print(tup1)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.

# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When choosing a collection type, it is useful to understand the properties of that type. 
# Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.