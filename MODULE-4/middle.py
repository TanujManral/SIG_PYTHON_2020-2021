a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a>b:
    if a<c:
        middle=c
    elif b>c:
        middle=b
    else:
        middle=a
else:
    if a>c:
        middle=a
    elif b<c:
        middle=b
    else:
        middle=c

print("The middle element amongst all 3 is", middle)
