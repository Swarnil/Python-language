n=int(input("Enter the number : "))
ps=0
ng=0
ze=0
for i in range(0,n):
    x=int(input("Enter no. : "))
    if (x>0):
        ps=ps+1
    elif (x<0):
        ng=ng+1
    else :
        ze=ze+1
print("Posetive numbers : ", ps)
print("Negative numbers : ", ng)
print("Zeros : ", ze)
     
