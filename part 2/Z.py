n=int(input("Enter Any Number: "))
for i in range(1,n+1,1):
    print("* ",end='')
print("")
for k in range(1,n-1,1):
    for j in range(n-k,1,-1):
        print(" ",end=' ')
    print("*")
for i in range(1,n+1,1):
    print("* ",end='')