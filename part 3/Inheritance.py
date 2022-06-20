# Inheritance
class A:
    def __init__(self,n,r):
        self.name=n
        self.roll=r
class B:
    def __init__(self,n,r):
        A.__init__(self,n,r)
class C(A,B):
    def __init__(self,n,r):
        B.__init__(self,n,r)
    def show(self):
        print(self.name)
        print(self.roll)
obj2=C("Tanu",2)
obj2.show()



