# # #Classes and objects
# class Addition:
#     def GetData(self):
#         self.n=int(input("Enter 1st Number: "))
#         self.n1=int(input("Enter 2nd Number: "))
#     def AddData(self):
#         c=self.n+self.n1
#         print(f"Addition of {self.n} and {self.n1} is {c}")
# obj=Addition()
# obj.GetData()
# obj.AddData()


# Constructor
# class Student:
#     def __init__(self,n,r):
#         self.roll=r
#         self.name=n
#     def ShowData(self):
#         print("Name: ",self.name)
#         print("Roll :",self.roll)
# obj=Student('Gopal',19)
# obj.ShowData()
#
# obj2=Student('Avik',10)
# obj2.ShowData()

class Student:
    count=0
    def __init__(self,n):
        Student.count += 1
        self.roll=Student.count
        self.name=n
    def __str__(self):
        return "Name: "+self.name +"Roll: "+ self.roll"
obj=Student('Gopal')
print(obj)
obj2=Student('Avik')
print(obj2)


