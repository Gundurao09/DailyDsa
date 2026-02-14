"""
Docstring for day_3_pattern

problem Statement: Print this pattern

1
12
123
1234
12345

"""

def number_pattern(n):
    for row in range(1,n+1):
        for col in range(row,n+1):
            print(row, end=" ")
        print()
print(number_pattern(5))