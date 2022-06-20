#SUBMITTED BY GOPAL SARKAR
# 1. WAP in python to reverse a string using user defined function.
def StrRev(n):
    for i in range(len(n)-1,-1,-1):
        print(n[i],end='')
n=input("Enter Any String: ")
StrRev(n)
# ========================================================================================

# 2. WAP in python to print fibonacci series in reverse order using user defined function.
# INPUT : 22
# OUTPUT : 21 13 8 5 3 2 1 1 0
def RevFibo(n):
    a,b,sum=0,1,0
    list=[]
    for i in range(n):
        a = b
        b = sum
        sum = a + b
        if b<=n:
            list.append(b)
        else:
            break
    list.reverse()
    return list
n=int(input("Enter The Limit: "))
print(RevFibo(n))
# ======================================================================================

# 3. WAP in python to count the vowel characters present in a string.
#     Write vowelCount(s) function to count and return the count.abs
#     INPUT: Siliguri, Darjeeling, WB
#     OUTPUT: Vowel count = 7
def VowelCount(s):
    count=0
    for i in s:
        if i in['a','e','i','o','u','A','E','I','O','U']:
            count+=1
    return count
s=input("Enter Any String: ")
print(VowelCount(s))
# ========================================================================================

# 4. WAP in Python to create a function checkLargest(x,y,z) which will return the largest among the three numbers.
def CheckLargest(a,b,c):
    if (a >= b and a >= c):
        return a
    if (b >= a and b >= c):
        return b
    if (c >= a and c >= b):
        return c
x=int(input("Enter 1st Number: "))
y=int(input("Enter 1st Number: "))
z=int(input("Enter 1st Number: "))
print(CheckLargest(x,y,z))
# ========================================================================================
# 5. WAP in python to explain the concept "function inside of function".
def outer():
    n=int(input("Enter Any Number: "))
    def inner(n):
        print(f"Squre of {n} is {n*n} ")
    inner(n)
outer()
