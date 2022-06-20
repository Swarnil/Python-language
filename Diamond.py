n=int(input("Enter The Limit: "))
count = 0
middle = 1
for i in range(0,n,1):
    for k in range(i,n-1,1):
        print(" ",end='')
    for j in range(1,2,1):
        print("*",end='')
    for s in range(1,i+1,1):
        print(" ",end='')
    for mid in range(1,i,1):
        print("",end=' ')
    if count!=0:
        for last in range(1,2,1):
            print("*",end='')
    count=count+1    
    print("")

count=0
for l in range(0,n-1,1):
    for g in range(0,l+1,1):
        print(" ",end='') 
    for m in range(1,2,1):
        print("*",end='')
    for k in range(g,n-2,1):
        print(" ",end='')
    for t in range(g,n-3,1):
        print(" ",end='')        
    for last in range(1,2,1):
        if count!=n-2:
            print("*",end='')
    count=count+1           
    print("")
  