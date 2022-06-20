# Passing Function as a argument in another function
def process(insert):
    c = x + y
    return c

def insert():
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    return a, b

x, y = insert()
s = process(insert)
print("Result is: ", s)
