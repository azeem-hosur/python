# Append Items
# To add an item to the end of the list, use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("mango")
print(thislist)

# Insert Items
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index

thislist.insert(2,"orange")
print(thislist)

thislist2 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist2.extend(tropical)
print(thislist2)

# The elements will be added to the end of the list.

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)

thislist3 = ["apple", "banana", "cherry"]
thistuple = ("mango","orange")
thislist3.extend(thistuple)
print(thislist3)