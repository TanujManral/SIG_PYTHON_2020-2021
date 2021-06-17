max= int(input(" Enter the Maximum Value : "))
total = 0

for num in range (max+1):
    if(num % 2 == 0):
        total = total + num

print("The Sum of Even Numbers from 1 to {0} = {1}".format(num, total))