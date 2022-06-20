# #Number 1
# str=input("Enter Your Name")
# for i in range(5):
#     print(str[i],end='')

# Number 3
# dict={}
# str='institute'
# for i in str:
#     if i in('a','e','i','o','u'):
#         keys=dict.keys()
#         # print(keys)
#         if i in keys:
#             dict[i]+=1
#         else:
#             dict[i] =1
# print(dict)

#Number 4
# n=int(input("Enter Limit:"))
# sum=0
# for i in range(n+1):
#     sum=sum+i
# print(sum)

#Number 6
# def small(l):
#     l.sort()
#     return l[2]
# l=[34,89,54,20,50,76,10,45,90]
# print(small(l))

# Number 5
# str='00011110000001010111010'
# count=0
# l=[]
# for i in range(1,len(str)):
#     if str[i-1]==str[i]:
#         count+=1
#     else:
#         l.append(count)
#         count=0
# print(l)
# print(max(l)+1)

#Balloon = Bal*o*n
def Balloon(str):
    if len(str) > 1:
        print(str[0], end='')
        for i in range(1, len(str)):
            if str[i - 1] == str[i]:
                print('*', end='')
            else:
                print(str[i], end='')
    else:
        print('empty string')
str = input("Enter a String: ")
Balloon(str)