n=int(input("Enter The Limit: "))
for i in range(0,n,1):
    for k in range(i,n-1,1):
        print(" ",end='')
    for j in range(0,i+1,1):
        print("* ",end='')
    print("\n")

for l in range(0,n,1):
    for g in range(0,l+1,1):
        print(" ",end='') 
    for m in range(l,n-1,1):
        print("* ",end='')
    print("\n")
