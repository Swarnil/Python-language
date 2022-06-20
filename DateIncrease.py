class MyClass:
    def __init__(self):
        self.d=int(input("Enter Day (eg:1-31): "))
        self.m=int(input("Enter Month (eg:1-12): "))
        self.y=int(input("Enter Year (eg: 2012): "))
        print(f"Your Inserted Date is: {self.d}.{self.m}.{self.y}")

    def addDays(self):
        n=int(input("Enter Number of days to be added: "))
        temp_d=self.d+n
        temp_m=self.m
        print(temp_d)
        if self.y%4!=0:
            if temp_m == 1:
                if temp_d > 31:
                    self.d=temp_d-31
                    self.m=2
                else:
                    self.d=self.d+n

            if self.m == 2:
                if temp_m > 28:
                    self.d = temp_d - 28
                    self.m=3
                else:
                    self.d=self.d+n
            if temp_m == 3:
                if temp_d > 31:
                    self.d = temp_d - 31
                    self.m=4
                else:
                    self.d=self.d+n
            if temp_m == 4:
                if temp_d > 30:
                    self.d = temp_d - 30
                    self.m=5
                else:
                    self.d=self.d+n
            if temp_m == 5:
                if temp_d > 31:
                    self.d = temp_d - 31
                    self.m=6
                else:
                    self.d=self.d+n
            if temp_m == 6:
                if temp_d > 30:
                    self.d = temp_d - 30
                    self.m=7
                else:
                    self.d=self.d+n
            if temp_m == 7:
                if temp_d > 31:
                    self.d = temp_d - 31
                    self.m=8
                else:
                    self.d=self.d+n
            if temp_m == 8:
                if temp_d > 31:
                    self.d = temp_d - 31
                    self.m=9
                else:
                    self.d=self.d+n
            if temp_m == 9:
                if temp_d > 30:
                    self.d = temp_d - 30
                    self.m=10
                else:
                    self.d=self.d+n
            if temp_m == 10:
                if temp_d > 31:
                    self.d = temp_d - 31
                    self.m=11
                else:
                    self.d=self.d+n
                    self.m = 11
            if temp_m == 11:
                if temp_d > 30:
                    self.d = temp_d - 30
                    self.m=12
                else:
                    self.d=self.d+n
            if temp_m == 12:
                if temp_d > 31:
                    self.d = temp_d - 31
                    self.m=1
                    self.y=self.y+1
                else:
                    self.d=self.d+n
        print(f"New Date is: {self.d}.{self.m}.{self.y}")

obj=MyClass()
obj.addDays()