# Boolean Values
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer

print(10>20)
print(10==10)
print(5<3)


# When you run a condition in an if statement, Python returns True or False
a = 10
b = 20

if a>b:
    print(f"{a} is greater than {b}")
elif b>a:
    print(f"{b} is greater than {a}")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello"))
print(bool(10))

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
print(bool(5))
print(bool("hello"))
print(bool(["car","bike"]))

# Some Values are False
# In fact, there are not many values that evaluate to False, 
# except empty values, such as (), [], {}, "", the number 0, 
# and the value None. And of course the value False evaluates to False.

print(bool(0))
print(bool(""))
print(bool([]))

# One more value, or object in this case, evaluates to False, 
# and that is if you have an object that is made from a 
# class with a __len__ function that returns 0 or False:
class myclass():
    def __len__(self):
        return 0

myObj = myclass()
print(bool(myObj))

# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:
def myfunc():
    return True

print(myfunc())

# You can execute code based on the Boolean answer of a function:
if myfunc():
    print("Yes")
else:
    print("No")

# Python also has many built-in functions that return a boolean value, 
# like the isinstance() function, which can be used to determine 
# if an object is of a certain data type:
# Check if an object is an integer or not:
x = 100
print(isinstance(x, int))