# def sum(a,b):
#     s=a+b
#     a=a+1
#     b=b+2
#     print(a)
#     print(b)
#     print(s)
# a=10
# b=20
# sum(a,b)
# print(a)
# print(b)
# ==============================================================================
# x=10
# def sum():
#     x=20 #Local Variable
#     print(x)
#     x=x+1
# sum()
# print(x)
# ================================================================================
# x=10
# def sum():
#     global x #Global Variable
#     print(x)
#     x=x+1
# sum()
# print(x)
# ==================================================================================

# def outer():
#
#     x=10
#     print(x)
#     def inner():
#         nonlocal x #It only works in nested function for passing the value to outer function
#         x=20
#         print(x)
#     inner()
#     print(x)
#
# x=5
# outer()
# print(x)
# ================================================================
#The Maximum Limit of Recursion in python is 1000
# s=0
# def sum(s):
#     s+=1
#     if s<6:
#         print("Hi")
#         sum(s)
# sum(s)
# ====================================================================
# def sum(s):
#     s=s-1
#     if s>0:
#         sum(s)
#     print(s)
# sum(5)
# ================================================================================
#HOME WORK


# ========================================================================

# ==============================================================================
# def length(s):
#     return rev(s)
# g= 'Gopal'
# print(length(g))

# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return s[-1]+reverse(s[:-1])
# s="Gopal"
# print(reverse(s))


# def reverse(s):
#
#   if s == '':
#     return s
#   else:
#     last = s[-1]     #last letter 'a'
#     rest = s[:-1]   #rest of the 'sitmc'
#
#   1st= last + reverse(rest)  #'a' + 'sitmc'
#   2nd
# s = input("Enter any string: ")
# print(reverse(s))
