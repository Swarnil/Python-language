# n = int(input("Enter Any Number:"))
# flag = 0
# for i in range(2,n-1,1):
#     if(n%i == 0):
#         flag = 1
# if flag == 1:
#     print("Not Prime")
# else:
#     print("Prime")

# def main():
#     n = int(input("Enter Any Number:"))
#     flag = 0
#     for i in range(2, n - 1, 1):
#         if (n % i == 0):
#             flag = 1
#     if flag == 1:
#         print("Not Prime")
#     else:
#         print("Prime")
# if __name__=="__main__":
#     main()
#


# def main():
#     n = int(input("Enter Any Number:"))
#     for i in range(2,n):
#         if(i%i+1==0):
#             print(i)
#
# if __name__=="__main__":
#     main()





# def series(n):
#     for i in range(1,n+1,2):
#         print(i,end=" ")
# n=int(input("Enter Any Number: "))
# series(n)



# def odd(n):
#     if n%2!=0:
#         print("Odd")
#     else:
#         print("Even")
# n=int(input("Enter Any Number: "))
# odd(n)



# def large(num1,num2,num3):
#     if (num1 >= num2) and (num1 >= num3):
#         largest = num1
#     elif (num2 >= num1) and (num2 >= num3):
#         largest = num2
#     else:
#         largest = num3
#     return largest
# num1=int(input("Enter 1st Number: "))
# num2=int(input("Enter 2nd Number: "))
# num3=int(input("Enter 3rd Number: "))
# l=large(num1,num2,num3)
# print("largest Number is :",l)


# def fact(n):
#     f=1
#     for i in range(2,n+1):
#         f=f*i
#     return f
# n=int(input("Enter Any number: "))
# g=fact(n)
# print("Facorial of {} is {}".format(n,g))


# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             print(i,end=" ")
#         print()
#
# n=int(input("Enter Limit: "))
# pattern(n)



# def revr(n):
#     rem=0
#     rev=0
#     while n != 0:
#         rem = n % 10
#         rev = rev * 10 + rem
#         n = n // 10
#     return rev
# n=int(input("Enter Any Integer: "))
# g=revr(n)
# print(g)

# def fibo(n):
#     a = 0
#     b = 1
#     sum = 0
#     count = 1
#     while (count <= n):
#         print(sum, end=" ")
#         count =count+1
#         a = b
#         b = sum
#         sum = a + b
# def main():
#     fibo(10)
# if __name__=="__main__":
#     main()
#

# def compare(n):
#     f=(9*n+160)/5
#     print(bool(n==f))
# def main():
#     n=float(input("Enter Temperature in Celsius: "))
#     compare(n)
# if __name__=="__main__":
#     main()


# def test(n):
#     for i in range(2,n):
#         for j in range(i,n):
#             if n%i==0:
#                 r=i
#                 print(r)
#                 g=n//i
#                 n=g
#                 if n%i!=0 and n==i:
#                     print(n)
#     if n>2:
#         print(n)
# test(24)
#


# def prime(m):
#     count = 0
#     for i in range(2, m):
#         if (m % i == 0):
#             count = 1
#             break
#     if count == 0:
#         return m
# def main(n):
#     i=2
#     while i<=n:
#         if prime(i):
#             if n%i==0:
#                 print(i)
#                 n=n/i
#                 continue
#         i=i+1
# main(16)


# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#        f = f*i
#     return f
# def sum(n)
#     s=0
#     for i in range(1,n):
#         s=s+i+fact(i)
#     print(sum)
# sum(10)
