a=[1,2,3,4,5,6,7,8,9]
b=[]
for j in a:
    if(j%2==0):
        b.append("#")
    else:
        b.append(j)
print(a)
print(b)