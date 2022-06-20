
# # ======================================================================================>

# # =======================================================================================>

# # =========================================================================================>
# #::::a+a+a+a .... (a=a,b=n)::::
# def multiplies(a,b):
#   if a == 0 or b == 0:
#     return 0
#   else:
#     while b > 0:
#       b -= 1
#       return a + multiplies(a,b)
#
# a,b = map(int,input("Enter the value of a and b: ").split())
# print(multiplies(a,b))
# # ===============================================================================================
# #::::PRINT ALL DIGITS IN REVERSE ORDER::::
# def digits(n):
#     if n == 0:
#         return
#     else:
#         print(n % 10, end=",")
#         digits(n // 10)
#
#
# n = int(input("Enter a number: "))
# digits(n)
# # ==========================================================

# Reverse integer and print each digit
