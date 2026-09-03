# Python Logical Operators
# Logical operators are used to combine conditional statements. Python has three logical operators:

# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true
# The and Operator
# The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.

# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both condition are True")

# The or Operator
# The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.

# Example
# Test if a is greater than b, OR if a is greater than c:

if a > b or a > b:
    print("At least one of the condition is True")

# The not Operator
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement.

# Example
# Test if a is NOT greater than b:
if not b > c:
    print("a is not greater than b")

# Combining Multiple Operators
# You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or.

# Example
# Combining and, or, and not:

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")

# Truth Tables
# Understanding how logical operators work with different values:

# and Operator Truth Table
# Condition 1	    Condition 2	            Result
# True	            True	                True
# True	            False	                False
# False	            True	                False
# False	            False	                False

# or Operator Truth Table
# Condition 1	    Condition 2	            Result
# True	            True	                True
# True	            False	                True
# False	            True	                True
# False	            False	                False


# Using Parentheses for Clarity
# When combining multiple logical operators, use parentheses to make your intentions clear and control the order of evaluation.
# Example
# Using parentheses for complex conditions:
temp = 25
is_raining = False
is_weekend = True
if  (temp > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor")

# More Examples
# Example
# User authentication check:
username = "Azeem"
password = "123"
is_verified = True

if username and password and is_verified:
    print("Login successful")
else:
    print("Login failed")

# Example
# Range checking with logical operators:

score = 85

if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")