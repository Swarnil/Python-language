def PrimeCheck(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
    if(flag==1):
        print("It's Not a Prime Number: ")
    else:
        print("It's a Prime Number")
n=int(input("Enter Any Number: "))
PrimeCheck(n)