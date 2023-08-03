### Exercise 2: Find the Largest Number in a List

# Write a Python function to find the largest number in a given list using loops.

list = [1, 2, 5, 10, 1, 11, 8]
# def find_largest(list):
#     return max(list)

def find_largest(list):
    largest = list[0]
    for num in list:
        if num > largest:
            largest = num
    return largest

print(find_largest(list))
numbers = [23, 45, 12, 67, 34, 89]
print(find_largest(numbers))