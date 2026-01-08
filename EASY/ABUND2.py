# Print Abundant Numbers in The range N

# Numbers upto the range N is checked whether it is an abundant number or not. For more reference , Check Problem Number 3

# A number that is smaller than the sum of all its factors except the number itself is known as an abundant number 

# Code:


num = int(input("Enter the number : "))
add = 0 
for i in range(1, num):
    if (num % i == 0):
        add = add + i
        
if (num < add):
    print(f'{num} is an abundant number')
else:
    print("It is not an abundant number")