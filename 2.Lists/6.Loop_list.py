# Loop Through a List
# You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for i in thislist:
    print(i)

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.
for i in range(len(thislist)):
    print(thislist[i])

# The iterable created in the example above is [0, 1, 2].

# Using a While Loop
# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
[print(x) for x in thislist]