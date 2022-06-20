def reverse(n,l):
    if n>0:
        rem = n % 10
        if(rem not in l):
            l.append(rem)
        n = n // 10
        reverse(n,l)
    return l
l = []
n=int(input("Enter Any Number: "))
print(reverse(n,l))