"""
Docstring for day_3_count_occurrences_array

Problem Statement: Count occurrences of a number in an array


Input:
arr = [1, 2, 3, 2, 4, 2, 5]
target = 2

Output:
3

Rules
No count() function
Only loops

Time Complexity: O(n)
Space Complexity: O(1)
"""

def count_occurrence(arr, target):
    count = 0

    for ele in arr:
        if ele == target:
            count += 1

    return count

# def count_occurrence(arr, target):
#     d = {}
#     for ele in arr:
#         if ele in d:
#             d[ele] += 1 
#         else:
#             d[ele] = 1

#     return d.get(target, 0)


arr = list(map(int, input("Enter the element(Int): ").split()))
target = int(input("Enter the Target number: "))

print(f"The Occurrences of {target} is: {count_occurrence(arr, target)}")
