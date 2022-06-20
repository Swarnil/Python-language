# # Input an integer and print each digit
def reverse(n):
    if n>0:
        rem = n % 10
        n = n // 10
        reverse(n)
        print(rem)
n=int(input("Enter Any Number: "))
reverse(n)