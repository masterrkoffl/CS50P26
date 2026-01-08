# Find the Sum of the First N Natural Numbers

# Given a Natural Number of N, we need to find the sum of all the natural numbers until the value of N. We can use different methods to write the Python code and one of the most effective method is using For Loop.

# Code:


range = int(input("Enter the ranges: "))
add = 0
for  i in range(range+1):
     add = add + i 

print(f"The sum of the first {ranges} numbers is {add}")