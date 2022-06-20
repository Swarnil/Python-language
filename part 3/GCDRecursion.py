#GCD Using Recursion
def gcd(a, b):
    if (b == 0):
        return a
    else:
        if a>b:
            return gcd(b, a % b)
        elif b>a:
            return gcd(a, b % a)
a =int(input("Enter 1st Number:"))
b =int(input("Enter 2nd Number: "))
print("GCD of {} and {} is:".format(a,b),gcd(a, b))