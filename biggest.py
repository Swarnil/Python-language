def big(l):
    global n,b
    for i in range(n):
        if l[i]>b:
            b=l[i]
    return b
l=[]
n=int(input("How Many Number: "))
for i in range(n):
    g=int(input("Enter Value: "))
    l.append(g)
b=l[0]
print(big(l))