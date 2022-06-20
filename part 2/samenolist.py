i=0
l1 = eval(input("Enter the values of the list: "))
print(l1)
while i<len(l1)-1:
    while l1[i]==l1[i+1]:
        l1.remove(l1[i+1])
    i=i+1
        
print(l1)
