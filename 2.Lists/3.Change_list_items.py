# Change Item Value
# To change the value of a specific item, refer to the index number

thislist = ["apple", "banana", "cherry"]
thislist[1] = "mango"
print(thislist)

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, 
# and refer to the range of index numbers where you want to insert the new values
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist2[2:4] = ["grapes","watermelon"]
print(thislist2)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Example
# Change the second value by replacing it with two new values:
thislist3 = ["apple", "banana", "cherry"]
thislist3[1:2] = ["mango","kivi"]
print(thislist3)

# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

# If you insert less items than you replace, the new items will be inserted where you specified, 
# and the remaining items will move accordingly
# Example
# Change the second and third value by replacing it with one value:
thislist4 = ["apple", "banana", "cherry"]
thislist4[1:3] = ["kivi"]
print(thislist4)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:

thislist5 = ["apple", "banana", "cherry"]
thislist5.insert(2,"kivi")
print(thislist5)

# Note: As a result of the example above, the list will now contain 4 items.