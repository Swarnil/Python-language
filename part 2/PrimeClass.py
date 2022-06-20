class PrimeCheck:
    def __init__(self,g):
        self.n=g
    def Check(self):
        flag = 0
        for i in range(2, self.n//2):
            if self.n % i == 0:
                flag = 1
        if flag == 1:
            print("It's Not a Prime Number: ")
        else:
            print("It's a Prime Number")
if __name__=='__main__':
    number = int(input("Enter Any Number: "))
    obj=PrimeCheck(number)
    obj.Check()