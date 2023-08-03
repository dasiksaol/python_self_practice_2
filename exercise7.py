### Exercise 7: Prime Numbers in a Range

# Write a Python function to find all prime numbers within a given range.

number = input("Number: ")

def prime(number):
    list = []
    number = int(number)
    for i in range(1, number):
        if i > 1:
            for j in range(1, i):
                if j > 1 and (i % j) == 0:
                    break
            else:
                list.append(i)
                
    return list
    
print(prime(number))
# print(prime(10))
