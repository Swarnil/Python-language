# l3=[1,2,3,[12,13],'ABC']
# print(l3[3])

# m = [0,0,0,0]
# m = [0]*4
# print(m)

# arr=[[0]*3]*4
# print(arr)

# a = eval(input("Enter Number: "))
# print(a)
# lst1=['Avik','Gopal']
# print(lst1)
# lst2=[1,2,3]
# print(lst2)
# print(lst1*2)
# print(lst1+['Avipsa'])
# print(lst1+lst2)


#lst1 = ['Avik','Gopal','Rajarshi','Tanushree','Arghadipdas']
#lst2 = [1,2,3,9,5]

# print(len(lst2))
# print(max(lst1)) It will not return the largest valus, it will return alphabetically maximum value
# print(min(lst1))
#print(sum(lst2))
# print(4 in lst2)

#lst2.append(7)
#print(lst2)

#lst2.append(['a','b'])
#lst2.append('MCA')
#lst2.extend('MCA')

# print(lst2.count(2))

lst2 = [1,2,3,4,5,6,7,8,9]
# lst2.pop(2) Remove by position
# print(lst2)

lst2.remove(9) #remove by value, if multiple value , then only first will delete

#del lst2[1:5:1]
# lst2.insert(2,[10,20,30])
#lst2.reverse()
#print(lst2)

gopal = [0]*5
gopal = [[0]*5]*4
gopal = [i*i for i in range (len(gopal)*4)]
print(gopal)
