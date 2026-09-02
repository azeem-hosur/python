# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# But there are some workarounds.

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

t1 = ("apple","banana","grapes","mango")
t2 = list(t1)
t2[1] = "kiwi"
t1 = tuple(t2)
print(t1)

# Add Items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
t1 = ("apple","banana","grapes","mango")
t2 = list(t1)
t2.append("cherry")
t1 = tuple(t2)
print(t1)

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), 
# create a new tuple with the item(s), and add it to the existing tuple
t3 = ("apple","mango")
t4 = ("orange",)
t3 += t4
print(t3)

# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

# Remove Items
# Note: You cannot remove items in a tuple.

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
t1 = ("apple","banana","grapes","mango")
t2 = list(t1)
t2.remove("apple")
t1 = tuple(t2)
print(t1)

# Or you can delete the tuple completely:

# Example
# The del keyword can delete the tuple completely:
t1 = ("apple","banana","grapes","mango")
del t1
print(t1) # Error