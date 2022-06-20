import numpy as np
# # #1 Number
# # import numpy as np
# # n=int(input("Enter Last Digit: "))
# # a=np.arange(1,n,2)
# # print(a)
# #
# # #2 Number
# # b=a.reshape(-1,1)
# # print(b)
#
# # 3 Number
# s=np.random.rand(6)
# print(s)
#
# #4 Number
# d=s.reshape(2,3)
# print(d)
#
# #5 Number
# s1=np.random.rand(6)
# print(s1)
#
# # #6 Number
# # sum=np.add(s,s1)
# # print(sum)
# # sub=np.subtract(s,s1)
# # print(sub)
# # mul=np.multiply(s,s1)
# # print(mul)
# # div=np.divide(.p,s1)
# # print(div)
#
# #7 Number
# s=s.reshape(2,3)
# s1=s1.reshape(3,4)
# print(np.dot(s,s1))

# Add Row in 2D Array
g=np.array([1,2,3,4,5,6,7,8,9])
g=g.reshape((3,3))
print(g)

gs=np.append(g,[[10,11,12]],axis=1)
print(gs)

