# Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

# Example
# A function with one argument:
def my_func(fname):
    print(fname + " hosur")

my_func("azeem")

# Parameters vs Arguments
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the actual value that is sent to the function when it is called.

# Example
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument


# Number of Arguments
# By default, a function must be called with the correct number of arguments.

# If your function expects 2 arguments, you must call it with exactly 2 arguments.

# Example
# This function expects 2 arguments, and gets 2 arguments::

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# If you try to call the function with the wrong number of arguments, you will get an error:

# Default Parameter Values
# You can assign default values to parameters. If the function is called without an argument, it uses the default value:

def greet(name = "friend"):
   print(f"Hello {name}")

greet("Azeem")
greet()

# Keyword Arguments
# You can send arguments with the key = value syntax.

# Example
def info(name,age):
   print(f"My name is {name} and my age is {age}")

info(age=26, name="azeem")

# This way, with keyword arguments, the order of the arguments does not matter.

# The phrase Keyword Arguments is often shortened to kwargs in Python documentation.

# Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.

# Positional arguments must be in the correct order:
info("azeem",26)
info(26,"azeem") # wrong

# The order matters with positional arguments:

# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.

# However, positional arguments must come before keyword arguments
def myfunc(animal, name, age):
   print(f"I have a {age} year old {animal} animal")

myfunc("cat", name="meow", age = 5)

# Passing Different Data Types
# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

# The data type will be preserved inside the function:

# Example
# Sending a list as an argument:

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# Example
# Sending a dictionary as an argument:

def f1(person):
   print(f"Name: {person["name"]}")
   print(f"Age: {person["age"]}")

my_per = {
    "name" : "Azeem",
    "age": 26
}

f1(my_per)

# Return Values
# Functions can return values using the return statement:

def add(x,y):
   return x + y

res = add(5,3)
print(res)

# Returning Different Data Types
# Functions can return any data type, including lists, tuples, dictionaries, and more.

# Example
# A function that returns a list:

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Example
# A function that returns a tuple:
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments.

# To specify positional-only arguments, add , / after the arguments:
def f2(name,/):
   print("hello", name)

f2("azeem")

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(name):
  print("Hello", name)

my_function(name = "Emil")

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def f3(*, name):
   print("hello", name)

f3(name="azeem")

# Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:
def f3(name):
   print("hello", name)

f3("azeem")

# Combining Positional-Only and Keyword-Only
# You can combine both argument types in the same function.

# Arguments before / are positional-only, and arguments after * are keyword-only:

# Example
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)