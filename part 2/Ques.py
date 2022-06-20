#1st Question With Built-In Function
# str1 = input("Enter 1st String: ")
# str2 = input("Enter 2nd String: ")
# str1=str1.replace(" ", "")
# srt2=str2.replace(" ", "")
# if str1 == str2:
#     print("They Are Same")
# else:
#     print("Not Same")

#Without Built-In Function
# str1 = input("Enter 1st String: ")
# str2 = input("Enter 2nd String: ")
# l1,l2=[],[]
# for i in range(len(str1)):
#     if str1[i]!=' ':
#         l1.append(str1[i])
# for i in range(len(str2)):
#     if str2[i - 1] != ' ':
#         l2.append(str2[i])
# if l1 == l2:
#     print("Same")
# else:
#     print("Not Same")



#5th Question
# t,t1=0,0
# s=int(input("Enter Salary: "))
# if s<=200000:
#     print("No Tax")
# if s>200000:
#     if s<300000:
#         t=(s-200000)*5//100
#         print(t)
#     else:
#         t1=(100000*5)//100
# if s>=300000:
#     if s<500000:
#         t=t1+(s-300000)*10//100
#         print(t)
#     else:
#         t1=t1+(200000*5)//100
# if s>500000:
#     if s<1000000:
#         t=t1+(s-300000)*15//100
#         print(t)
#     else:
#         t1=t1+(700000*15)//100
# if s>1000000:
#     t=t1+(s-300000)*15//100
#     print(t)
#
#
# 6th Question
def fact(f):
    if f==1:
        return f
    else:
        return f*fact(f-1)

f=int(input("Enter Any Number: "))
print(fact(f))

