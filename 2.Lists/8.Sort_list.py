# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

list1 = [6,4,9,10,54,23,12]
list1.sort()
print(list1)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
list2 = [6,4,9,10,54,23,12]
list2.sort(reverse=True)
print(list2)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):

def myfunc(n):
    return abs(n - 50)

list3 = [100, 50, 65, 82, 23]
list3.sort(key = myfunc)
print(list3)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list.

# So if you want a case-insensitive sort function, use str.lower as a key function:
list4 = ["banana", "Orange", "Kiwi", "cherry"]
list4.sort(key= str.lower)
print(list4)

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?

# The reverse() method reverses the current sorting order of the elements.
list5 = ["banana", "Orange", "Kiwi", "cherry"]
list5.reverse()
print(list5)