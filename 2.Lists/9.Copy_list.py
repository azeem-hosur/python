# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, 
# and changes made in list1 will automatically also be made in list2.

l1 = ["apple","mango"]
l2 = l1
l2.append("banana")
print(l1)

l3 = l1.copy()
l3.append("orange")
print(l3)
print(l1)

# Use the list() method
# Another way to make a copy is to use the built-in method list().

l4 = ["apple", "banana", "cherry"]
l5 = list(l4)
print(l5)

# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator.
l6 = ["apple", "banana", "cherry"]
l7 = l6[:]
print(l7)
