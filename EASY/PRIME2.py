# Print the Prime Numbers in a Given Range

# flag is Used To Assume a number is prime , on every new outerloop , the value is resetted to 0 
Code


range = int(input("Enter the range you want: "))

for i in range(2, range):
    flag = 0 
    for j in range(2, i):
        if (i % j == 0):
            flag  = 1
            break
    if (flag == 0):
        print(i)