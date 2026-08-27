# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Legal variables
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variables
# 2myvar = "John"
# my-var = "John"
# my var = "John"

a = 10
print(a)

_a = 20
print(_a)

Age_25 = 25
print(Age_25)

this_Is_Camel_Case = "this_Is_Camel_Case"
print(this_Is_Camel_Case)

This_Is_Pascal_Case = "This_Is_Pascal_Case"
print(This_Is_Pascal_Case)

this_is_snake_case = "this_is_snake_case"
print(this_is_snake_case)

"""
Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

Camel Case
Each word, except the first, starts with a capital letter:

myVariableName = "John"
Pascal Case
Each word starts with a capital letter:

MyVariableName = "John"
Snake Case
Each word is separated by an underscore character:

my_variable_name = "John"

"""