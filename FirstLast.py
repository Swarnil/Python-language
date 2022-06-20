import array
n = int(input("Enter Any Number: "))
rev = 0
count = 0
arr = []
count = 2
final = 0
while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    arr.append(rem)
    n = n // 10
temp = arr[0]
for i in range(1, len(arr)-3, 1):
    temp = arr[i]
    arr[i] = arr[len(arr)-count]
    arr[len(arr)-count] = temp
    count = count+1
for i in range(0, len(arr), 1):
    final = (final*10)+arr[i]
print(final)