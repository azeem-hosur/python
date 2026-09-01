# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator	            Description	                                                               Example
# in 	        Returns True if a sequence with the specified value is present in the object	    x in y	
# not in	    Returns True if a sequence with the specified value is not present in the object	x not in y

a = ["car", "bike", "ship"]
print("car" in a)

print("plane" not in a)

# Membership in Strings
# The membership operators also work with strings:
x = "Hello"
print("H" in x)
print("b" in x)
print("z" not in x)