
# def flat(l,l2):
#     if len(l)==0:
#         return list2
#     else:
#         for i in l:
#             if type(i) != list:
#                     l2.append(i)
#             else:
#                 flat(i,l2)
#     return l2
# l=[1,2,3,[4,5,6],7,8,[9,10,11]]
# l2=[]
# # print(list)
# print(flat(l,l2))



# def flatten(S):
#     if S == []:
#         return S
#     if isinstance(S[0], list):
#         return flatten(S[0]) + flatten(S[1:])
#     return S[:1] + flatten(S[1:])
# s=[[1,2],[3,[7,8,9],4]]
# print("Flattened list is: ",flatten(s))
#
#
# g=[[0]*5]*4
# print(g)

# l=[0]*5
# l1=l
# l1[0]=10
# print(l)
# print(id(l[0]))
# print(id(l[1]))


# import copy
# g=[[0]*4]*3
# g2=copy.deepcopy(g)
# g2[0]=10
# print(g)
# print(g2)

# g=[0 for i in range(4)]
# print(g)
# print(id(g[0]))
# print(id(g[1]))
# print(g[0] is g[1])

# g=[[0 for i in range(4)]
#    for x in range(3)]
# g[0][0]=10
# print(g)
# print(id(g[0]))
# print(id(g[1]))
