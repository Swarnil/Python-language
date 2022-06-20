n=int(input("Enter a number : "))
even=0
odd=0
while n>0:
    s=n%10
    if s==0:
        pass
    elif s%2==0:
        even = even+1
    elif s%2 != 0:
        odd = odd+1
    n=n//10
print("Number of even digit ", even)
print("Number of odd digit ", odd)
