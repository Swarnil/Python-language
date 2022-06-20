class ArmStrong:
    def __init__(self,n):
        self.n1=n
        self.count=0
    def getLength(self,n):
        while self.n1!=0:
            self.n1=self.n1//10
            self.count+=1
        self.n1=n
        return self.count
    def checkArm(self,n,count):
        final=0
        while self.n1!=0:
            rem=self.n1%10
            temp=rem**count
            final=final+temp
            self.n1=self.n1//10
        if final==n:
            return True
        else:
            return False
n=int(input("Enter Any Number: "))
obj=ArmStrong(n)
c=obj.getLength(n)
print(obj.checkArm(n,c))