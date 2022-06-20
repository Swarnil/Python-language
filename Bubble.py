l=[15,20,28,18,30,60,43,25]
j=len(l)
while j>0:
    for i in range(0,j-1):
        if(l[i]>l[i+1]):
            t=l[i]
            l[i]=l[i+1]
            l[i+1]=t
    j-=1
print(l)