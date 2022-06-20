# # Single Inheritance
# class A:
#     def getdata(self):
#         self.n=int(input("Enter Any Number: "))
# class B(A):
#     def showdata(self):
#         print(self.n)
# obj=A()
# obj2=B()
# obj2.getdata()
# obj2.showdata()

# #Multilevel Inheritance
# class A:
#     def getdata(self):
#         self.n=int(input("Enter Any Number: "))
# class B(A):
#     def sqr(self):
#         self.s=self.n*self.n
#         print("Squre is : ",self.s)
# class C(B):
#     def check(self):
#         if self.s%2==0:
#             print("Even Number")
#         else:
#             print("Odd Number")
# obj=C()
# obj.getdata()
# obj.sqr()
# obj.check()


# #Multiple Inheritance
# class A:
#     def getdata(self):
#         self.x=int(input("Enter 1st Number: "))
# class B():
#     def getdata2(self):
#         self.y=int(input("Enter 2nd Number: "))
# class C(A,B):
#     def add(self):
#         c=self.x+self.y
#         print("Addition is: ",c)
# obj=C()
# obj.getdata()
# obj.getdata2()
# obj.add()

# Hierarchical Inheritance
# class A:
#     def getdata(self):
#         self.n=int(input("Enter Any Number: "))
# class B(A):
#     def sqr(self):
#         self.n=self.n*self.n
#         print("Squre is : ",self.n)
# class C(A):
#     def check(self):
#         if self.n%2==0:
#             print("Even Number")
#         else:
#             print("Odd Number")
# obj=B()
# obj.getdata()
# obj.sqr()
#
# obj2=C()
# obj2.getdata()
# obj2.check()

#Hybrid Inheritance
class A:
    def getdata(self):
        self.n=int(input("Enter Any Number: "))
class B(A):
    def sqr(self):
        self.s=self.n*self.n
        print("Squre is : ",self.s)
class C(A):
    def cube(self):
        self.c=self.n*self.n*self.n
        print("Cube is: ",self.c)
class D(B,C):
    def add(self):
        a=self.s+self.c
        print("Addition is:",a)

obj3=D()
obj3.getdata()
obj3.sqr()
obj3.cube()
obj3.add()

#
