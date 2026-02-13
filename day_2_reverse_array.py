"""
Docstring for day_2_reverse_array

Problem Statement: Reverse an Array

Input 1: [1, 2, 3, 4, 5]
output: [5, 4, 3, 2, 1]

Input2: [4, 2, 7, 1, 9, 3]
output: [3, 9, 1, 7, 2, 4]

Rules
1.No arr[::-1]
2.No reverse()
3.You must not create a new array

Time Complexity: O(n)
Space Complexity: O(1)

"""

def reverse_arr(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        # swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        # move pointers
        left+=1
        right-=1

    return arr # return the same array


arr = list(map(int, input("Enter the element(Int): ").split()))

print(f"The Original array is: {arr}")

print(f"The Reverse array is: {reverse_arr(arr)}")