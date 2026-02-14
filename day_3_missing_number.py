"""
Docstring for day_3_missing_number

Problem Statement: Missing Number

Input: [1, 2, 4, 5, 6]
Output: 3

Input: [2, 3, 1, 5]
Output: 4


"""


def missing_number(arr):
    n = len(arr)+1
    expected_sum = n*(n+1)//2
    actual_sum = 0
    for ele in arr:
        actual_sum+=ele
    return expected_sum - actual_sum

arr = list(map(int, input("Enter the element(Int): ").split()))

print(f"The missing number is: {missing_number(arr)}")
