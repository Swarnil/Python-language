# n=(input("Enter Any String: "))
# count=0
# print(n[0].upper(),".",end="")
# for i in range(0,len(n)):
#     if n[i]==" ":
#         count+=1
#         print(n[i+1].upper(),".",end="")
# print("\nTotal Space: ",count)


n=(input("Enter Any String: "))
count=0
print(n[0].upper(),".",end="")
for i in range(0,len(n)): #For Counting Total Space
    if n[i] == " ":
        count+=1
space=0
for i in range(0,len(n)):
    if n[i] == " ":
        space+=1
        if(space<count):
            print(n[i+1].upper(),".",end="")
        else:
            print(n[i+1].upper(),end="")
            break
print(n[i+2:])
