#1.  A positive integer m can be expresseed as the sum of three squares if it is of the form p + q
# + r where p, q, r ≥ 0, and p, q, r are all perfect squares. For instance, 2 can be written as
# 0+1+1 but 7 cannot be expressed as the sum of three squares. The first numbers that cannot
# be expressed as the sum of three squares are 7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, …
import math
m=int(input("Enter Any Number: "))
def threesquares(m):
   if m>=0:
       x=list(range(0,math.floor(math.sqrt(m)+1)))
       print(x)
       for i in x:
           for j in x:
               for k in x:
                   if (i**2)+(j**2)+(k**2)==m:
                        return True
       else:
            return False
   else:
       return False
print(threesquares(m))

#=================================================================================

# # 2. Write a function repfree(s) that takes as input a string s and checks whether any
# # character appears more than once. The function should return True if there are no repetitions
# # and False otherwise.
def repfree(s):
    flag=0
    for i in range(len(s)):
        j = i + 1
        while j!=len(s):
            if s[i]==s[j]:
                flag=1
                break
            else:
                j+=1
    if flag==1:
        print("False")
    else:
        print("True")
s=input("Enter Any String: ")
repfree(s)


