n = int(input("Enter the number:  "))
l = ("hi world")
try:
    a = 12/n
    print(a)
    print(l[n])
    print("Hello World")
except ZeroDivisionError:
    print("!!!Exeption Caught!!!")
except:
    print("handle all exceptions")
else:
    print("Exception didnt occur")
finally:
    print("Must Exicute")
