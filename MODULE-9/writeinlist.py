abc = [1,2,3,4,5,6,7,8]
with open('abc.txt', "w") as myfile:
        for c in abc:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())