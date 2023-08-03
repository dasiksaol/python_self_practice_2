### Exercise 4: Calculate the Sum of a 2D List

# Write a Python function to calculate the sum of all elements in a 2D list.

list = [[1, 10, 10], [2, 5, 6], [1, 5, 6]]

def sum_list(list):
    total = 0
    for x in list:
        total += sum(x)
    return total


print(sum_list(list))