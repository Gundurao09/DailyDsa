"""
Docstring for day_2_Digital Root

Problem Statement: digit_sum of digits until single digit

Input 1 : 9875
Output: 2
Explanation:
9+8+7+5 = 29
2+9 = 11
1+1 = 2

Input 2 : 38
Output: 2
Explanation:
3+8 = 11
1+1 = 2

Time Complexity: O(d)
Space Complexity: O(1)

"""

def digital_root(n):

    while n >= 10: # loop run until the number is greater then 10
        digit_sum = 0 # initialize the digit_digit_sum = 0

        while n > 0: # loop run until the number is greater then 0
            digit = n % 10 # it give the remainder
            digit_sum += digit # add the remainder
            n //= 10 # using floor to divide the number

        n = digit_sum

    return n # return number

n = int(input("Enter the number: "))

print(digital_root(n))
    