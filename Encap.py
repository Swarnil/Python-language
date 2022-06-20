class A:
    def __init__(self,n,r):
        self.name=n
        self.__roll = r
    def Show(self):
        print('Name: ',self.name)
        print('Name: ', self.__roll)
ob=A("Gopal",1)
ob.Show()
print(ob.name)
# print(ob.__roll) #error

