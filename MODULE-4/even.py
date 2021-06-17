beginning=int(input("Enter the starting number :\n"))
end=int(input("Enter the ending number :\n"))

for num in range(beginning, end + 1):  
    if num % 2 == 0: 
        print(num, end = " ")