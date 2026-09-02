# Add Items
# Once a set is created, you cannot change its items, but you can add new items.

# To add one item to a set use the add() method.
s1 = {"apple","banana","mango"}
s1.add("cherry")
print(s1)

# Add Sets
# To add items from another set into the current set, use the update() method.
# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)