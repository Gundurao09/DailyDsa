"""
Docstring for day_2_second_largest_element

Problem Statement: Find The Second Largest Element in an Array

Input 1:  [5, 2, 9, 1, 7]
Output: The Second Largest Element in an Array is : 7

Input 2:  [8, 5, 6, 9, 7]
Output: The Second Largest Element in an Array is : 8

Time Complexity: O(n)
Space Complexity: O(1)

"""
# Create a function name as second_largest()
def second_largest(arr):
    if len(arr) < 2:
        return "Not enough elements"

    large_ele = arr[0] # initialize max as first element
    sec_larg_ele = float('-inf')

    for i in range(1,len(arr)): # using loop check if the current element is greater then first element put into the list
        
        if arr[i] > large_ele:
            sec_larg_ele = large_ele
            large_ele = arr[i]
        elif arr[i] > sec_larg_ele and arr[i] != large_ele:
            sec_larg_ele = arr[i]

    return sec_larg_ele # return the second largest element

arr = list(map(int, input("Enter the element(Int): ").split()))

print(f"The Second Largest Element in an Array is: {second_largest(arr)}")
    