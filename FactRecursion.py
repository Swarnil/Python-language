# #Factorial of a natural number using recursion
f=1
def fact(n):
    global f
    f=f*n
    n=n-1
    if n>0:
        fact(n)
    return f
n=int(input("Enter Any Number: "))
print("Factorial of {} is:".format(n),fact(n))