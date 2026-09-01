# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# Operator	    Description	                                                Example
# is 	        Returns True if both variables are the same object	        x is y	
# is not	    Returns True if both variables are not the same object	    x is not y

x = ["apple","Banana"]
y = ["apple","Banana"]
z = x

print(x is y)
print(x is z)
print(x == y)
print(x is not y)

# Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
# Example
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)