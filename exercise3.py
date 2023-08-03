### Exercise 3: Reverse a String

# Write a Python function to reverse a given string using loops.

def reverse_string(str):
    new_string = ""
    for x in str[::-1]:
        new_string += x
    return new_string

print(reverse_string("Hello"))
