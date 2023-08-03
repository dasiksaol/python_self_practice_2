### Exercise 8: Fibonacci Sequence

# Write a Python function to generate the Fibonacci sequence up to a given number.

def fibonacci(num):
    temp = 0
    list = []
    for i in range(1,num-1):
        if i == 0:
            continue
        elif i == 1:
            list.append(temp)
            list.append(i)
            new = list[i-1] + list[i]
            list.append(new)
        else:
            new = list[i-1] + list[i]
            list.append(new)
        
        
    print(list)

fibonacci(10)



