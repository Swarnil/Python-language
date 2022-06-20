class Student:
    r=0
    def __init__(self,n):
        Student.r+=1
        self.name=n
        self.roll=Student.r
    def ViewData(self):
        print(f"Name is: {self.name}")
        print(f"Roll is: {self.roll}")
    def __del__(self):
        print("Destructor Call")
obj=Student('Gopal')
obj.ViewData()
obj2=Student('Avik')
obj2.ViewData()
obj3=Student('Suvankar')
del obj3
print("Example of Destructor")

