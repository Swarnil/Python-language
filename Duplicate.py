# Input - 1126234   Output - [4, 3, 2, 6, 1]
list = []
def rev(n):
  global list
  if n>0:
    rem = n % 10
    if rem not in list:
      list.append(rem)
    rev(n//10)
    return list
print(rev(1126234))