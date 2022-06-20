from functools import reduce

l = [10,15,28,30,51,63,92]
t = reduce(lambda a,b : a+b, l)
print(t)
