# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
a = "Hello Azeem"
print(a[6])

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for b in "Azeem":
    print(b)

# String Length
# To get the length of a string, use the len() function.

c = "Hello"
print(len(c)) # 5

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in
a = "This is a text"
print("text" in a) # True

# Use it in an if statement
if "text" in a:
    print("Yes text is present in a")

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in
print("azeem" not in a)