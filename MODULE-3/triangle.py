
l1= int(input("ENTER THE 1st SIDE OF THE TRIANGLE:\n"))
l2= int(input("ENTER THE 2nd SIDE OF THE TRIANGLE:\n"))
l3= int(input("ENTER THE 3rd SIDE OF THE TRIANGLE:\n"))

if l1 == l2 == l3:
	print("ITS AN Equilateral Triangle")
	
elif l1==l2 or l2==l3 or l3==l1:
	print("ITS AN Isosceles Triangle")
	
else:
	print("ITS AN Scalene Triangle")