#
# #Shallow Copy
# l=[0]*5
# l1=l
# l1[0]=10
# print(l)
# print(id(l[0]))
# print(id(l1[0]))
#
# # Deep Copy
# import copy
# l=[0]*4
# l2=copy.deepcopy(l)
# l2[0]=10
# print(l)
# print(id(l[0]))
# print(id(l2[0]))

import copy
a=10
b=20
b=copy.deepcopy(a)

print(id(a))
print(id(b))