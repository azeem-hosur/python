# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

a = "Hello Azeem"
print(a[2:7])

# Slice From the Start
# By leaving out the start index, the range will start at the first character

b = "Hello Python"
print(b[:3])

# Slice To the End
# By leaving out the end index, the range will go to the end
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string
c = "Azeem"
print(c[-4:-2])
