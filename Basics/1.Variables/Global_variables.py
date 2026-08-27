# Global Variables

# Variables that are created outside of a function are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
x = "Hello"

def myfun():
    print(x)

myfun()
print(x)

# If you create a variable with the same name inside a function, this variable will be local, 
# and can only be used inside the function. The global variable with the same name will remain
# as it was, global and with the original value.

a = "Mohammad"

def myfun2():
    a = "Azeem"
    print("Local variable",a)

myfun2()
print("Global variable",a)

# Normally, when you create a variable inside a function, 
# that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

def myfun3():
    global b 
    b = "Python"

myfun3()
print("Global variable",b)

# Also, use the global keyword if you want to change a global variable inside a function.
# To change the value of a global variable inside a function, 
# refer to the variable by using the global keyword:

c = "This is python"

def myfun4():
    global c 
    c = "Hello Python"

myfun4()
print("Global variable",c)
