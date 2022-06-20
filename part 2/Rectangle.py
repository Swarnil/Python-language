class Rectangle:
    def GetData(self,l,b):
        self.length=l
        self.breath=b

    def PrintData(self):
        print("***** Inside PrintData Function ******")
        print("Length: ",self.length)
        print("Breath: ",self.breath)

    def Area(self):
        print("***** Inside Area Function ******")
        self.a=self.length*self.breath
        print("Area: ",self.a)
l=int(input("Enter Length: "))
b=int(input("Enter Breath: "))
obj=Rectangle()
obj.GetData(l,b)
obj.PrintData()
obj.Area()

