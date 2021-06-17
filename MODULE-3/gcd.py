def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

n=int(input("Enter the 1st number\n"))

m=int(input("Enter the 2nd number\n"))


hcf = compute_hcf(m,n)
print("The HCF of the 2 number is:", hcf)