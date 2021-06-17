a=["HI","IPL","YOYO","AM","TANUJ","Manral","I"]
max1=0
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print("The word with the longest length in the List is: "+ str(temp))