def fact():
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input("Enter The Number :"))
g=fact()
print("Factorial of {} is {}" .format(n,g))