def fun(x):
    return(lambda y : x+y)
a = fun(3)
b = fun(10)
print(a(5))
print(b(5))
