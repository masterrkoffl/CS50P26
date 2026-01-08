# Find the Sum of the digits of a number

# Each digit of a number is taken and added to get the required result

# Example : N = 180, SUM = 1 + 8 + 0 = 9

# Code:

num = int(input("Enter a number : "))

add = 0 

while (num!=0):
    reminder = num % 10
    add = add + reminder 
    num = num // 10
    
print(add)