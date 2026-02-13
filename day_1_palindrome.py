"""
Docstring for day_1_Palindrome

Problem Statement: Check if a number is a Palindrome (WITHOUT converting to string)

Input: 121
Output: True

Input: 123
Output: False

Important Rule:
You cannot do:

str(n) == str(n)[::-1]

Time Complexity: O(d)
Space Complexity: O(1)

"""
# Create a function name as ispalindrome()
def ispalindrome(num):
    temp = num # Store num in temp variable
    res = 0 # Initializes res = 0

    while temp > 0: # Using while loop reverse the number
        rem = temp % 10
        res = res * 10 + rem
        temp //= 10

    return num == res # check if the num is palindrome it return true otherwise return false

num = int(input("Enter the number:"))

if ispalindrome(num):
    print(f"{num} is Palindrome.")
else:
    print(f"{num} is not Palindrome.")


