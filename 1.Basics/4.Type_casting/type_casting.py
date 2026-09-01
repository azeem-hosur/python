# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

x = int(5)
y = int(10.5)
z = int("3")

print(x)
print(y)
print(z)

a = float(2)
b = float(2.2)
c = float("5")
d = float("4.2")

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

e = str("x")
f = str(2)
g = str(4.5)
h = str(54.55)

print(e,type(e))
print(f,type(f))
print(g,type(g))
print(h,type(h))