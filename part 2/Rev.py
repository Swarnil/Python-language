n = int(input("Enter Any Number:"))
rev = 0
rem = 0
while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
print(rev)

# n=int(input("Enter Any Number:"))
# last=n%10
# middle=n-10000
# t=middle//10
# first=n//10000N
# sum=0
# sum=(sum+last*10)+(middle*10)+first*10

# print(last,end='')
# print(t,end=' ')
# print(first,end=' ')

# print(sum)

