# # for i in range(5):
# #     print(i,end='')
# #     if i==1:
# #         continue
# #     else:
# #         print("end")
# #
# a=[1,2,8,3,5]
# a.sort()
# print(a)
# b=sorted(a)
# print(b)


# x=['bvik','aviks']
# x.sort(key=len)
# print(x)

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.

# s=input(("Enter Any String: "))
# if(len(s))<=2:
#     print(s)
# else:
#     print(s[:2],end='')
#     for i in range(len(s)-4):
#         print('*',end='')
#     print(s[-2::1])
#

# s=input(("Enter Any String: "))
# if(len(s))<=2:
#     print(s)
# else:
#     f=s[0]
#     print(f,end='')
#     for i in range(1,len(s)):
#         if f != s[i]:
#             print(s[i],end='')
#         else:
#             print('*',end='')


# n=int(input("Enter any number: "))
# m=n*9
# sum=0
# print(m)
# while sum!=9:
#     sum=0
#     while m!=0:
#         sum=sum+m%10
#         m=m//10
#     m=sum
# print("Yes the addition is ",sum)

# g="Welcome to  Siliguri"
# x=g.split()
# print(x)

# values = input("Enter 3 number: ").split()
# a, b, c = map(int, values)
# print(a, b, c)

# x=0
# while x<20:
#      x=x+3
# print(x)

# Python3 program to find date after adding
# given number of days.

# Return if year is leap year or not.
def isLeap(y):
     if (y % 100 != 0 and y % 4 == 0 or y % 400 == 0):
          return True
     return False


# Given a date, returns number of days elapsed
# from the beginning of the current year (1st
# jan).
def offsetDays(d, m, y):
     offset = d
     switcher = {
          10: 30,
          9: 31,
          8: 30,
          7: 31,
          6: 31,
          5: 30,
          4: 31,
          3: 30,
          2: 31,
          1: 28,
          0: 31
     }
     if (isLeap(y) and m > 1):
          offset += 1
     offset += switcher.get(m)
     return offset


# Given a year and days elapsed in it, finds
# date by storing results in d and m.
def revoffsetDays(offset, y, d, m):
     month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

     if (isLeap(y)):
          month[2] = 29
     for i in range(1, 13):
          if (offset <= month[i]):
               break
          offset = offset - month[i]

     d[0] = offset
     m[0] = i + 1


# Add x days to the given date.
def addDays(d1, m1, y1, x):
     offset1 = offsetDays(d1, m1, y1)
     if isLeap(y1):
          remDays = 366 - offset1
     else:
          remDays = 365 - offset1

     # y2 is going to store result year and
     # offset2 is going to store offset days
     # in result year.
     if (x <= remDays):
          y2 = y1
          offset2 = offset1 + x
     else:

          # x may store thousands of days.
          # We find correct year and offset
          # in the year.
          x -= remDays
          y2 = y1 + 1
          if isLeap(y2):
               y2days = 366
          else:
               y2days = 365

          while (x >= y2days):
               x -= y2days
               y2 += 1
               if isLeap(y2):
                    y2days = 366
               else:
                    y2days = 365

          offset2 = x

     # Find values of day and month from
     # offset of result year.
     m2 = [0]
     d2 = [0]
     revoffsetDays(offset2, y2, d2, m2)
     print("d2 = ", *d2, ", m2 = ", *m2, ", y2 = ", y2, sep="")


# Driven Program
d = 14
m = 3
y = 2015
x = 366

addDays(d, m, y, x)

# This code is contributed by shubhamsingh10
