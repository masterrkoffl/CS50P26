# Find whether a number is perfect square or not

# Examples of Perfect Number : 4, 9, 16, 25 etc

# Code : 

import math

num = int(input("Enter the number : "))

result1 = int(math.sqrt(num))

if float(result1) == math.sqrt(num):
    print("Yes")
else:
    print("No")