# *args and **kwargs
# By default, a function must be called with the correct number of arguments.

# However, sometimes you may not know how many arguments that will be passed into your function.

# *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguments - *args
# If you do not know how many arguments will be passed into your function, add a * before the parameter name.

# This way, the function will receive a tuple of arguments and can access the items accordingly:

# ExampleGet your own Python Server
# Using *args to accept any number of arguments:

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Arbitrary Arguments are often shortened to *args in Python documentation.

# What is *args?
# The *args parameter allows a function to accept any number of positional arguments.

# Inside the function, args becomes a tuple containing all the passed arguments:

# Example
# Accessing individual arguments from *args:
def func(*args):
    print(f"Type: {type(args)}") # <class 'tuple'>
    print(f"First arg: args[0]")
    print(f"Second arg: args[1]")
    print(f"all {args}")

func("Mohammad","azeem","hosur",25)

# Using *args with Regular Arguments
# You can combine regular parameters with *args.

# Regular parameters must come before *args:

# Example

def f1(greet, *names):
    for name in names:
        print(f"{greet} {name}")

f1("Hii","azeem","azeem25")
# In this example, "Hello" is assigned to greeting, and the rest are collected in names.

# Practical Example with *args
# *args is useful when you want to create flexible functions:

# Example
# A function that calculates the sum of any number of values:

def cal_sum(*num):
    total = 0
    for n in num:
        total += n
    return total

print(cal_sum(1,2,4,5))
print(cal_sum(1,2,4,5,50))
print(cal_sum(5))

# Example
# Finding the maximum value:
def max_val(*num):
    max = num[0]
    for n in num:
        if n > max:
            max = n
    return max

print(f"Max val is {max_val(4,6,12,343,43)}")
print(f"Max val is {max_val(4,634,123,343,43,23)}")

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

# This way, the function will receive a dictionary of arguments and can access the items accordingly:

# Example
# Using **kwargs to accept any number of keyword arguments:

def func(**kid):
    print(f"His last name is {kid["lname"]}")

func(fname = "azeem", lname = "hosur")

# Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentation.

# What is **kwargs?
# The **kwargs parameter allows a function to accept any number of keyword arguments.

# Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

# Example
# Accessing values from **kwargs:

def myfunc(**kwargs):
    print(f"Type: {type(kwargs)}")
    print(f"Name : {kwargs["Name"]}")
    print(f"Age: {kwargs["age"]}")
    print(f"All: {kwargs}")

myfunc(Name = "azeem", age = 26, lastname = "hosur")

# Using **kwargs with Regular Arguments
# You can combine regular parameters with **kwargs.

# Regular parameters must come before **kwargs:

# Example
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function.

# The order must be:

# regular parameters
# *args
# **kwargs
# Example
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# Unpacking Arguments
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

# Unpacking Lists with *
# If you have values stored in a list, you can use * to unpack them into individual arguments:

# Example
# Using * to unpack a list into arguments:

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

# Unpacking Dictionaries with **
# If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname":"azeem", "lname":"hosur"}
my_function(**person)
my_function(person) # error

# Remember: Use * and ** in function definitions to collect arguments, and use them in function calls to unpack arguments.