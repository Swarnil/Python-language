#Matrix Addition
r=int(input("Enter Number Of Rows: "))
c=int(input("Enter Number Of Column: "))
first=[]
second=[]
var=[]
sum=[]
print("**** Enter Values for 1st Matrix ****")
for i in range(0,r):
    for j in range(0,c):
        var.append(int(input("Insert Value For [{}][{}] :".format(i,j))))
    first.append(var)
    var=[]
print(first)

var=[]
print("**** Enter Values for 2nd Matrix ****")
for i in range(0,r):
    for j in range(0,c):
        var.append(int(input("Insert Value For [{}][{}] :".format(i,j))))
    second.append(var)
    var=[]
print(second)

print("**** Result Of Addition ****")
for i in range(0,r):
    for j in range(0,c):
        sum.append( first[i][j] + second[i][j])
print(sum)