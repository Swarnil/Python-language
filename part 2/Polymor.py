class box:
    def __init__(self,l,b,h):
        self.length=l
        self.breadth=b
        self.hight=h
    def ShowData(self):
        print("Length: ",self.length)
        print("Breadth: ",self.breadth)
        print("Hight: ",self.hight)
    def Volume(self):
        v=self.length*self.breadth*self.hight
        print("Volume: ",v)
    def __add__(self,B):
        l=self.length +B.length
        b=self.breadth + B.breadth
        h=self.hight+ B.hight
        b=box(l,b,h)
        return b
b1=box(2,3,4)
b2=box(1,1.2,3.2)
b1.ShowData()
b1.Volume()

b3=b1+b2
b3.ShowData()
b3.Volume()


