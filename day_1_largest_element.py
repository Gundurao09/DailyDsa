"""
Docstring for day_1_Largest Element

Problem Statement: Find the Largest Element in an Array
Input:
arr = [4, 2, 7, 1, 9, 3]
Output:
The Largest Element in an Array is: 9

Time Complexity: O(n)
Space Complexity: O(1)

"""

# Create a function name as largest()
def largest(arr):
    if not arr:          # handles empty list
        return "Array is empty"
    
    largest_ele = arr[0] # initialize max as first element

    for ele in arr[1:]: # using loop check if the first_element is larger then largest_ele update largest_ele
        if ele > largest_ele:
            largest_ele = ele

    return largest_ele # return largest_ele

arr = list(map(int, input("Enter the element(Int): ").split()))

print(f"The Largest Element in an Array is: {largest(arr)}")

