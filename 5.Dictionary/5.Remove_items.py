# Removing Items
# There are several methods to remove items from a dictionary:

# ExampleGet your own Python Server
# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop("year")
print(thisdict)

# Example
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.popitem()
print(thisdict)

# Example
# The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del thisdict["model"]
print(thisdict)

# Example
# The del keyword can also delete the dictionary completely:
del thisdict
# print(thisdict) # error

# Example
# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.clear()
print(thisdict) # {}