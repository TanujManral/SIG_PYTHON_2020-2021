sum = 0



list = []
n = int(input("Enter number of elements : "))
  

for i in range(0, n):
    element = int(input())
  
    list.append(element)
    
print(list)

for element in range(0, len(list)):
	sum = sum + list[element]

print("Sum = ", sum)
