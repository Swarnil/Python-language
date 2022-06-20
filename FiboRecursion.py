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