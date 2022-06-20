# #1st Question
# s="   my name,   is,       avik        gopal  "
# c=0
# g=0
# for i in s:
#     c+=1
# for i in range(c):
#     try:
#         if s[i]==' ' and s[i+1]!=' ':
#             g+=1
#     except IndexError:
#         pass
# if(s[0])!=' ':
#     print(g+1)
# else:
#     print(g)

#
# #2nd Question
# n=input("Enter Values: ")
# l=[]
# g=0
# c=0
# sum=0
# final=0
# g=0
# loop=0
# for i in n:
#     if i!=' ':
#         g=g*10+int(i)
#     else:
#         l.append(g)
#         g = 0
# l.append(g)
# print(l)
# for i in l:
#     c+=1
# for i in range(1,c,2):
#     try:
#         sum=(l[i]) *(l[i+1])
#         final=sum+final
#         loop+=1
#     except IndexError:
#         pass
# if l[0]==loop:
#     print(final)
# else:
#     print("Sorry, Invalid Input")

# #Solution of 3rd Question
# n=input("Enter Values: ")
# g,c,t=0,0,0
# l=[]
# for i in n:
#     if i!=',':
#         g=g*10+int(i)
#     else:
#         l.append(g)
#         g = 0
# l.append(g)
# for i in l:
#     c+=1
# for i in l:
#     t+=1
#     s = int((2 * 50 * i / 30) ** 0.5)
#     print(s,end='')
#     if t != c:
#         print(',', end='')

# #Solution of 4th Question
# class Rectangle:
#     length=0
#     breadth=0
#     def __init__(self):
#         self.length=int(input("Enter Length: "))
#         self.breadth=int(input("Enter Breadth: "))
#     def setLength(self):
#         self.length = int(input("Enter New Length : "))
#     def setBreadth(self):
#         self.breadth=int(input("Enter Breadth: "))
#     def getBreadth(self):
#         print(f"Breadth is {self.breadth}")
#     def Area(self):
#         print(f"Area is {self.length*self.breadth}")
#     def Perimeter(self):
#         print(f"Perimeter is: {(self.length+self.breadth)*2}")
#
# obj=Rectangle()
# obj.setLength()
# obj.setBreadth()
# obj.getBreadth()
# obj.Area()
# obj.Perimeter

#Solution of 5th question





