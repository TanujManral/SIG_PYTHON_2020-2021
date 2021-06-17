 
number=int(input("Enter the number:"))
sum=0
while(number>0):
    modulus=number%10
    sum=sum+modulus
    number=number//10
print("The total sum of digits is:",sum)