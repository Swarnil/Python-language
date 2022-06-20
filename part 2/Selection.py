# l = [1,2,'A',165]
# print(l)
# l.append('MCA')
# print(l)
# l.insert(3,36)
# print(l)
# l2 = l[2:]
# print(l2)
#
# l2.append([9,8,6])
# print(l2)
l=[15,20,28,18,3,60,43,25]
# l2=[]
for i in range(0,len(l)-1,1):
    for j in range(i+1, len(l), 1):
        if(l[i] > l[j]):
            swap = l[j]
            l[j] = l[i]
            l[i] = swap
print(l)
