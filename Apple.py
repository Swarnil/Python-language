n = int(input("How Many Boys: "))
arr = []
apple = 0
count = 0
for i in range(0, n, 1):
    num = int(input("Enter Apple For Boy {} : ".format(i + 1)))
    arr.append(num)
    apple = apple + arr[i]
sh = apple // n
print(arr)
print("Total Apple: ", apple)

if apple % n == 0:
    print("Apple Amount Matched")
    ind = n - 1
    while ind >= -1:
        if ind == n - 1:
            rind = 0
        else:
            rind = ind + 1

        if ind == 0:
            lind = n - 1
        else:
            lind = ind - 1

        while arr[rind] < sh < arr[ind]:
            arr[rind] = arr[rind] + 1
            arr[ind] = arr[ind] - 1
            count = count + 1
            print(arr)
        while arr[ind] > sh:
            arr[lind] = arr[lind] + 1
            arr[ind] = arr[ind] - 1
            count = count + 1
            print(arr)
        ind = ind - 1
    print("Total Steps: ", count)
else:
    print("Sorry {} Apples Not Divided By {}".format(apple, n))
