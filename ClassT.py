# Nth Position of  Fibonacci Series
a = 0
b = 1
sum = 0
count = 1
def fibo(n):
    global a,b,sum,count
    if count <= n:
        count =count+1
        a = b
        b = sum
        sum = a + b
        fibo(n)
    return sum
n=int(input("Enter The Position: "))
print("{}th Number Fibonacci Series is: ".format(n),fibo(n))
# ==============================================================
# String length count using recursion
def str_len(str):
  if str == '':
    return 0
  else:
    return 1 + str_len(str[1:])
v = str_len('SITMCA')
print(v)
# ==============================================================
#String Reverse using Recursion
def reverse(s):
  if s == '':
    return s
  else:
    last = s[-1]     #last letter 'a'
    rest = s[:-1]   #rest of the 'sitmc'
  return last + reverse(rest)  #'a' + 'sitmc'
s = input("Enter any string: ")
print(reverse(s))
# ==================================================================
Palindrome Using Recursion
def palindrom(str):
  if str == '':
    return True
  if len(str) == 1:
    return True
  if str[0] == str[-1] and palindrom(str[1:-1]):
    return True
  else:
    return False
print(palindrom('MACCAM'))

# =======================================================================
#  Write a recursive function that multiplies two positive numbers a and b ,
# and return the result . Multiplication is to be achieved as a+a+a...(b times)
c=0
def multi(a,b):
    global c
    c=c+a
    b=b-1
    if b>0:
        multi(a,b)
    return c
a=6
b=7
print(multi(a,b))
# =========================================================================
# Write a recursive function that takes number as input parameter
# and print all digit (Input- 1362 Output-1,3,6,2)
def reverse(n):
    if n>0:
        rem = n % 10
        n = n // 10
        reverse(n)
        print(rem)
n=int(input("Enter Any Number: "))
reverse(n)

# ===================================================================
# Reverse integer Using Recursion. Input-11362 Output-26311
def reverse(n):
    if n>0:
        rem = n % 10
        print(rem)
        n = n // 10
        reverse(n)
n=int(input("Enter Any Number: "))
reverse(n)
# =======================================================================
# Revese integer and store in list(without duplicate values) .Input- 1126234 Output [4,3,2,6,1]
# Input - 1126234   Output - [4, 3, 2, 6, 1]
list = []
def rev(n):
  global list
  if n>0:
    rem = n % 10
    if rem not in list:
      list.append(rem)
    rev(n//10)
    return list
print(rev(1126234))
# ===================================================================
#Flatten List
def flat(l,l2):
    if len(l)==0:
        return list2
    else:
        for i in l:
            if type(i) != list:
                    l2.append(i)
            else:
                flat(i,l2)
    return l2
l=[1,2,3,[4,5,6],7,8,[9,10,11]]
l2=[]
print(list)
print(flat(l,l2))
# ======================================================================
#2D List
g=[[0]*5]*4
print(g)

# ========================================================================
# Shallow Copy And Deep Copy

#Shallow Copy
l=[0]*5
l1=l
l1[0]=10
print(l)
print(id(l[0]))
print(id(l1[0]))

# Deep Copy
import copy
l=[0]*5
l2=copy.deepcopy(l)
l2[0]=10
print(l)
print(id(l[0]))
print(id(l2[0]))