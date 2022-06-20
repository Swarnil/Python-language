# class Student:
#     r=0
#     def __init__(self,n):
#         Student.r+=1
#         self.roll=Student.r
#         self.name=n
#     def ShowData(self):
#         print("Roll is: ",self.roll)
#         print("Name is: ",self.name)
#     def __del__(self):
#         print("Object Deleted")
# obj=Student("Gopal")
# obj.ShowData()
#
# obj2=Student("Avik")
# obj2.ShowData()
# del obj2
#
# obj3=Student("Suvankar")
# obj3.ShowData()
# print("Example of Destructor")


class sum:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def Show(self):
        print("1st Value is: ",self.x)
        print("2nd Value is",self.y)
    def Cal(self):
        c=self.x+self.y
        print("Result is",c)
    def __add__(self,g):
        a=self.x+g.x
        b=self.y+g.y
        n=sum(a,b)
        return n
obj=sum(2,3)
obj1=sum(4,5)
obj.Show()
obj.Cal()

obj2=obj+obj1
obj2.Show()
obj2.Cal()