# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

t1 = ("apple","banana","cherry")
for i in t1:
    print(i)

# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.
for i in range(len(t1)):
    print(t1[i])

# Using a While Loop
# You can loop through the tuple items by using a while loop.

# Use the len() function to determine the length of the tuple, 
# then start at 0 and loop your way through the tuple items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.
i = 0
while i < len(t1):
    print(t1[i])
    i = i + 1