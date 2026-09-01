# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

for x in list2:
    list1.append(x)

print(list1)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:
l1 = [1,2,3,4]
l2 = ["hello"]
l1.extend(l2)
print(l1)