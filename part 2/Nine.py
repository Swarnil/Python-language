def nine(n,sum):
    n=n*9
    def inner(n,sum):
        while n>0:
            rem = n % 10
            sum=sum+rem
            n = n // 10
        return sum
    t=inner(n,sum)
    if t==9:
        print(t)
    else:
        t=inner(t,sum)
        print(t)
n=int(input("Enter Any Number: "))
sum=0
nine(n,sum)
