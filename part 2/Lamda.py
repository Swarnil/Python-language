# def fun1(msg):
#     print("SIT",msg)
# def fun2(msg):
#     print("MCA",msg)
# def fun(f,m):
#     return f(m)
# fun(fun1,'Students')
# =====================================================
# x = lambda: print("Gopal Sarkar")
# x()
#======================================================
# y= lambda a:a*a
# print(y())
# ===================================================
# z= lambda a,b:a+b
# print(z(2,3))
#=================================
# y=lambda a,b:print("Result is:",a+b);
# n1=int(input("Enter 1st Number:"))
# n2=int(input("Enter 2nd Number:"))
# y(n1,n2)

# ========================================================
# def fun(x):
#     return lambda y: x + y
# t=fun(4) #4+y
# u=fun(10) #10+y
#
# print(t(5)) #4+5 =9
# print(u(7)) #7+10 =17
# ===========================================================

# l=[10,20,11,15,13,14,56,7,87,9,76,4,64,3]
# g=list(filter(lambda a:a%2!=0,l))
# print(g)


# l=[2,3,4,5,6,7,8,]
# g=list(filter(lambda a:a//3==2,l))
# print(g)

# l=[2,3,4,5,6,7,8,]
# g=list(map(lambda a:str(a),l))
# print(g)

# from functools import reduce
# l=[10,20,11,15,13,14,56,7,87,9,76,4,64,3]
# g=reduce(lambda a,b:a+b,l)
# print(g)

