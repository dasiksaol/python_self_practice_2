### Exercise 1: Print a Multiplication Table

# Write a Python program to print the multiplication table of a given number using nested loops.

n = input("Input Number: ") 
def multiplication(n):
    n = int(n)
    if n != 0:
        for x in range(1,11):
            print(f"{n} * {x} = {n * x}" )
        
print(multiplication(n))