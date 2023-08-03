### Exercise 9: Find Common Elements in Lists

# Write a Python function that takes two lists as input and returns a new list containing common elements between the two lists
list1 = [1, 2, 3, 3, 4]    
list2 = [3, 4, 5, 6, 7]

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

new = []
def common(list1, list2):
    for i in list1:
        for j in list2:
            if j in list1 and j not in new:
                new.append(j)
    return new

print(common(list1, list2))