list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input())
    list.append(element)
  
print(list,"\n")

print("Even Elements in the list are:")


for n in list:      
    if n % 2 == 0:
       print(n, end = " ")