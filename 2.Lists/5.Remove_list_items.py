# Remove Specified Item
# The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist2 = ["apple", "banana", "cherry","banana"]
thislist2.remove("banana")
print(thislist2)

# Remove Specified Index
# The pop() method removes the specified index.

thislist3 = ["apple", "banana", "cherry","banana"]
thislist3.pop(0)
print(thislist3)

# If you do not specify the index, the pop() method removes the last item.
thislist4 = ["apple", "banana", "cherry","banana"]
thislist4.pop()
print(thislist4)

# The del keyword also removes the specified index
thislist5 = ["apple", "banana", "cherry","banana"]
del thislist5[1]
print(thislist5)

# The del keyword can also delete the list completely.
thislist6 = ["apple", "banana", "cherry","banana"]
del thislist6
# print(thislist6) // Error

# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.
thislist7 = ["apple", "banana", "cherry","banana"]
thislist7.clear()
print(thislist7)