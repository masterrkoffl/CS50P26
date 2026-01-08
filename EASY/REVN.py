# Print the Reverse of a Number

# Code:

num = int(input("Enter a number: "))

temp = num
new = 0 
while (temp!=0):
    reminder = temp % 10 
    new = (new * 10) + reminder
    temp = temp // 10
    
print(new)