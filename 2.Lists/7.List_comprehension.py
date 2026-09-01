# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:

# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits2 if "a" in x]
print(newlist2)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

newlist3 = [x for x in fruits2 if x != "apple"]
print(newlist3)

# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

# The condition is optional and can be omitted

newlist4 = [x for x in fruits]
print(newlist4)

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.

list1 = [x for x in range(10)]
print(list1)

list2 = [x for x in range(10) if x < 5]
print(list2)

# Expression
# The expression is the current item in the iteration, but it is also the outcome, 
# which you can manipulate before it ends up like a list item in the new list
list3 = [x.upper() for x in fruits]
print(list3)

# You can set the outcome to whatever you like:
list4 = ["hello" for x in fruits]
print(list4)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
list5 = [x if x != "banana" else "orange" for x in fruits]
print(list5)