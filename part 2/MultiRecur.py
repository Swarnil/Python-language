# Multiplication Using Recursion without * sign
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

#::::a+a+a+a .... (a=a,b=n)::::
# def multiplies(a,b):
#   if a == 0 or b == 0:
#     return 0
#   else:
#     while b > 0:
#       b -= 1
#       return a + multiplies(a,b)
#
# a,b = map(int,input("Enter the value of a and b: ").split())
# print(multiplies(a,b))