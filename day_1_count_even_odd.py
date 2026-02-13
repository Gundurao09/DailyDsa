"""
Docstring for day_1_count_even_odd

Logic Building

Problem Statement: Count how many digits are even and odd in a number
Input: 52841
Output:
Even digits = 3
Odd digits = 2

Important Rule:
You cannot do:

digit % 2 == 0 and string

Time Complexity: O(n)
Space Complexity: O(1)

"""

def count_even_odd_int(number):
    number = abs(number)   # handle negative numbers
    even_count = 0
    odd_count = 0
    
    if number == 0:        # special case
        return 1, 0        # 0 is even

    while number > 0:
        digit = number % 10         # extract last digit
        odd_count += digit & 1      # 1 if odd, 0 if even
        even_count += (digit & 1) ^ 1  # 1 if even, 0 if odd
        number //= 10               # remove last digit
    
    return even_count, odd_count

# Example usage
num = int(input("Enter the number: "))
even, odd = count_even_odd_int(num)
print(f"Even digits: {even}, Odd digits: {odd}")

    


