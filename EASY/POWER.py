# Find the Power Of a Number using Iteration

# The Power of a number can be found in two methods.

# Code:

num, power = map(int, input("Enter the num and the power : ").split())

# Method 1 - Direct Exponentation

print(num ** power)

# Method 2 - Using Simple Iteration 

output = 1 
for i in range(power):
    output = output * num 
    
print(output)