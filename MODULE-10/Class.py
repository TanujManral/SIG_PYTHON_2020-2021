class student:

    def __init__(self, rollno,name): 
        self.rollno=rollno
        self.name=name


    def display(self):
        print("Name : "+self.name)
        print("Roll number : " +str(self.rollno))
        print("Age : "+ str(self.age))
        print("Marks : " + str(self.marks)+"\n")

    def setAge(self): 
        self.age=int(input("Enter age of " + self.name + ":"))


    def setMarks(self):
        self.marks=int(input("Enter marks of " + self.name + ":"))
        print("\n")



s1=student(1234,"TANUJ MANRAL") 
s2=student(5678,"NIDHI MANRAL")


s1.setAge()
s1.setMarks()
s2.setAge()
s2.setMarks()
s1.display()
s2.display()