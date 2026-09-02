# Access Items
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Loop through the set, and print the values:
s1 = {"apple","banana","mango"}
for i in s1:
    print(i)

# Check if "banana" is present in the set:
print("banana" in s1)

# Check if "banana" is NOT present in the set:
print("banana" not in s1)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.