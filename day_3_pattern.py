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
        for col in range(1,row+1):
            print(col, end="")
        print()

n = int(input("Enter the number to draw pattern"))

number_pattern(n)