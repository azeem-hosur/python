# The Ternary Operator
# The ternary operator allows you to assign one value if a condition is true, and another if it is false:

x = 6
y = "Weekend" if x > 5 else "Workday"
print(y)
# Note: The ternary operator is not an actual operator, it is a conditional expression, or a shorthand if statement.

# Instead of Elif:
# The ternary operator can be used instead of elif in longer if statements:

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)