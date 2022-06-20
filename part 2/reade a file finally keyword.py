n = int(input("Enter the number:  "))
try:
    a = 12/n
    print(a)
    print("Hello World")
except ZeroDivisionError:
    print("!!!Exeption Caught!!!")
finally:
    print("Must Exicute")

