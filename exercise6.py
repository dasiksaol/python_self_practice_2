### Exercise 6: Check for Palindrome

# Write a Python function to check if a given string is a palindrome (reads the same forwards and backwards).

word = input("word: ")
def palindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False
    
print(palindrome(word))