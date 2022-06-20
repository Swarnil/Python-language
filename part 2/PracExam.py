#1234 => 1324
n=int(input("Enter 4 Digit Number: "))
l=[]
final=0
while n!=0:
    rem=n%10 #For storing the last digit
    l.append(rem)
    n=n//10
temp=l[0]
l[0]=l[3]
l[3]=temp
for i in range(len(l)):
    #For converting list into integer
    final=(final*10)+l[i]
print(final)

# #0 2 1 4 1 8 2 16 3 32 5 64 8
# n=int(input("Enter Limit: "))
# count=0
# a,b,c,g=0,1,0,1
# for i in range(n):
#     if count!=n:
#         print(c,end=' ')
#         g=g*2
#         count+=1
#         if count!=n:
#             print(g,end=' ')
#             a=b
#             b=c
#             c=a+b
#             count+=1










