# Python has a set of built-in methods that you can use on strings.

# Upper Case
# The upper() method returns the string in upper case

a = "hello azeem"
print(a.upper())

# Lower Case
# The lower() method returns the string in lower case
b = "HELLO"
print(b.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end
c = " Hello  Azeem    "
print(c.strip())

# Replace String
# The replace() method replaces a string with another string:
d = "Hello Ayeem"
print(d.replace("y","z"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.
e = "Hello,World!"
print(e.split(","))
print(e.split("o"))
