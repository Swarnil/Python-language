# x = 100
# y=(1,2,3)
# print(type(y))
#Printing type of any variable----------------------------------------------------
# a=2+5j--------
# print(a)
# print(type(a))
# print(a.real)
# print(a.imag)

#List-----------------------------------------------------------------------------
# x=[1,2,3,4,5]
# print(x[0:])
# print(x[0:2])
# print(x[-1:0:-1])
# print(x[::-1]) #Print in reverse
# y=[0]*5
# print(y)

# print("Maximum Vslue: ", max(x))
# print("Minimum value: ", min(x))
# print("Length: ",len(x))
# print("Average: ",sum(x)//len(x)) #Printing Average

#Tuples------------------------------------------------------------------------
#Lists are  mutable, means we can modify it, But Tuples are immutable , means we can't modify it.
# city = () #Creting Empty Touple
# print(type(city))

# city = "Gangarampur","Siliguri"
# print(city)
# print(type(city))
#
# list=[1,2,3,4]
# tuple=(1,2,3,4)
# list.append(5)
# tuple.append(5) #It will not work as tuples are immutable
# print(list)
# print(tuple)

# Concatination of tuples
# tuple=(1,2,3,4)
# city= ("Gangarampur","Balurghat","Siliguri")
# print(tuple)
# print(city)
# print(type(city))
#
# mix=tuple+city #Concatinate one tuple to another tuple
# print(mix)
# print(type(mix))
#
#
# nest=(city,tuple) #Nested Tuples
#
# # nest=("Gopal ")*5
# print(nest)

#Slicing in Tuples
#
# tuple=(1,2,3,4)
# print(tuple[0:])
# print(tuple[::-1]) #Printing Reverse Order
#Unpacking
# g=tuple("SiliguriInstituteOfTechnology")
# print(g)
#Deleting Entire Tuple(Though tuples are immutable but we can delete it completely by using the del keyword)
# t=(1,2,3,4,5,6,7,8)
# del t
# print(t)

# t=(1,2,3,3,3,3,4,5,6,6,6,7,8)
# c=t.count(3)#It will count how many 3 are availabe in the particular tuple
# print(c)
#Nesting Lists with tuples
# t=(['a','b','c','d'],[1,2,3,4])
# print(t)
# t[0].append('e') #After Nesting lists in tuples we chan modify it easily
# t[1].append(5)
# print(t)

#Strings in Python-------------------------------------------------------------------------------
# str1 = 'Gopal' #We can use single quote or double quote
# print(str1)
#
# str1 = "Gopal's Birthday" #Whenever it occurs that single quote is need to use inside string then we can use double quote
# print(str1)
#
# str1 = 'Gopal Said "I am busy"' #Vice versa
# print(str1)
#
# str1 = 'Gopal said "It\'s my birthday"' #For using single and double quote at a time, we need to use \
# print(str1)
#
# str1 = '''My Name is
# Gopal Sarkar''' #For multiline string, we need to use 3 single or double quote
# print(str1)
#
# str1 = "Siliguri"
# for i in str1:
#     print(i)
#
# print(str1.upper())
# print(str1.lower())
# print(str1.find('g'))
# print(str1.index('g'))

# str1 = "Siliguri Institute of Tech"
# s=str1.split(" ")  #It will split the sentence whenever space found
# print(s)
#
# print(str1.replace("Tech","Technology"))

#Python Dictionaries Set ------------------------------------------------------------------------------
# d={}
# print(d)
# print(type(d))
#
# d2={1:"Siliguri",2:"Institute",3:"Of",4:"technology"}
# print(d2)
# #
# d3=({1:"Siliguri",2:"Institute",3:"Of",4:"technology"}) #Another method to create dictionary
# print(d3)
#
# d4={"Name":"Gopal", "Stream":"MCA", "City":"Gangarampur"} #Dictionary with string key value
# print(d4)
#
# d5={"Name":{"First":"Gopal", "Last":"Sarkar"}, "Stream":"MCA", "City":"Gangarampur"}
# print(d5)
#
# #Adding Elements to Dictionary
# d[0]="Welcome"
# print(d)
# d[1]=("Gopal","Sarkar")
# print(d)
# d["Name"]="Raju"
# print(d)
# print(d["Name"])

# d2={1:"Siliguri",2:"Institute",3:"Of",4:"technology"}
# print(d2.keys()) #Print Keys
# print(d2.values()) #Print Values

#if...else statement-------------------------------------------------------------------------

# n=int(input("Enter Marks: "))
# if n>=90 and n<=100:
#     print("O")
# elif n>=80:
#     print("E")
# elif n>=60:
#     print("A")
# elif n>=40:
#     print("B")
# else:
#     print("Fail")

#Loop in python --------------------------------------------------------------------------------------------
#A loop is a insturction that repeats multiple time as long as some condition is met
# n=int(input("Enter a Multiple of 7: "))
# while n%7 != 0:
#     n=int(input("Enter a Multiple of 7: "))
# else:
#     print("%d is a Multiple of 7" %n) #We can use else after while,,no need if.
# n=[[1,2,3,4],['a','b','c','d']]
# for i in n:
#     for j in i:
#         print(j,end=" ")
#     print()
#
# n="Hey There. How Are You?"
# for i in n:
#     if i=='.':
#         break
#     else:
#         print(i,end="")

# n="Hey There. How Are You?"
# for i in n:
#     if i=='.':
#         continue #It will skip full stop(.)
#     else:
#         print(i,end="")

# #Matrix Addition
# r=int(input("Enter Number Of Rows: "))
# c=int(input("Enter Number Of Column: "))
# first=[]
# second=[]
# var=[]
# sum=[]
# print("**** Enter Values for 1st Matrix ****")
# for i in range(0,r):
#     for j in range(0,c):
#         var.append(int(input("Insert Value For [{}][{}] :".format(i,j))))
#     first.append(var)
#     var=[]
# print(first)
#
# var=[]
# print("**** Enter Values for 2nd Matrix ****")
# for i in range(0,r):
#     for j in range(0,c):
#         var.append(int(input("Insert Value For [{}][{}] :".format(i,j))))
#     second.append(var)
#     var=[]
# print(second)
#
# print("**** Result Of Addition ****")
# for i in range(0,r):
#     for j in range(0,c):
#         sum.append( first[i][j] + second[i][j])
# print(sum)

# g=[1,2.4,"Gopal"]
# len=0
# i=0
# try:
#     while g[i]:
#         len+=1
#         i += 1
# except IndexError:
#     print(len)

# #Random Number
# import random
# ran= random.randint(100,999)
# print("Random Number is:",ran)
# n=int(input("Guess 3 Digit Number: "))
# count=0
# while n!=0:
#     r=n%10
#     r2=ran%10
#
#     n=n//10
#     ran=ran//10
#
#     if(r==r2):
#         count+=1
# if(count==3):
#     print("Your Guess is Right")
# elif(count>0 and count<3):
#     print("Right Guess Digit: ",count)
# else:
#     print("Sorry, Invalid Input")

#Array in Python
# from array import *
# n=array('i',[-1,2,3,4,5]) #here 'i' is for integer
# print(n)
#
# print(n.buffer_info())  # It will show the address and the size of tha array
#
# for i in n:
#     print(i) #print the array using loop
# for i in range(0,len(n)):
#     print(n[i]) #it will also print the array in the same way , but here the method is different
#
# n.reverse()
# print(n)
#
# n.append(10) #it will ad the value 20 at the last of the array
# print(n)
#
# n.remove(3) #It will delete the value 3 from the array,if there are more than one 3 then it will only delete the first one
# print(n)
# from array import * #Take empty array and insert value by user
# arr=array('i',[])
# n=int(input("Enter The Size Of Array: "))
# for i in range(0,n):
#     temp=int(input("Enter Value %d : "%i))
#     arr.append(temp)
#     print(arr[i])
# print(arr)

#Functions in Python --------------------------------------------------------------------------------------------------
# def add(a,b):
#     print("a: %d"%a)
#     print("b: %d"%b)
#     print(id(a))
#     print(id(b))
#     a=10
#     b=10
#     c=a+b
#     print(id(a)) #The id of a and b is different
#     print(id(b))
#     print("Addition is %d"%c)
# a=10
# b=20
# print("Outside Function")
# print(id(a))
# print(id(b))
# add(a,b)

# def add(*n):  #By using this method we can pass random number of parameters in functin
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(sum)
# add(10,20,30)

#Objects And Classes in Python ----------------------------------------------------------------
# class person:
#     def __init__(self,n,g,a):
#         self.name=n
#         self.gender=g
#         self.age=a
#     def talk(self):
#         print("My Name is: ",self.name)
#     def vote(self):
#         if self.age<18:
#             print("I Am Not Eligible For Vote")
#         else:
#             print("I Am Eligible For Vote")
# obj=person("Gopal","Male",23)
# obj1=person("Tanushree","Female",17)
# obj.talk()
# obj.vote()
#
# obj1.talk()
# obj1.vote()

#Inheritance
# class parent:
#     def show(self):
#         print("This is inside parent class")
# class child(parent):
#     def show2(self):
#         print("This is inside child class")
# obj=child()  #Creating object for child class
# obj.show2() #We can call the functions from both child and parent class ,by using the object of child class
# obj.show()

#Python Scripting ------------------------------------------------------------------------------------------------
# import time
# t=time.time()
# print(t)
# localtime=time.localtime(t)
# print(localtime)
# print(time.ctime(t))

#Function returning function
# def fun1():
#     x=10
#     def fun2(x):
#         x=x+1
#         return x
#     return fun2(x)
# s=fun1()
# print(s)

# g={'example',24,0.75,'a'}
# print(g)
