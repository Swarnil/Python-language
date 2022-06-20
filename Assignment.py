class MyDate:
    def __init__(self):
        self.d=int(input("Enter Day (eg:1-31): "))
        self.m=int(input("Enter Month (eg:1-12): "))
        self.y=int(input("Enter Year (eg: 2012): "))
        print(f">>Your Inserted Date is: {self.d}.{self.m}.{self.y}")

    def addDays(self):
        print("<<*** Inside addDays Function ***>>")
        n=int(input("Enter Number of days to be added: "))
        temp_d=self.d+n
        temp_m=self.m
        while temp_d>31:
            if temp_m in [1,3,5,7,8,10,12] and temp_d > 31:
                temp_d=temp_d-31
                temp_m+=1
                if temp_m>12:
                    temp_m=1
                    self.y=self.y+1
            if temp_m in [4,6,9,11] and temp_d>30:
                temp_d=temp_d-30
                temp_m += 1
                if temp_m > 12:
                    temp_m = 1
                    self.y=self.y+1
            if temp_m == 2 and self.y%4==0 and temp_d > 29:
                temp_d = temp_d - 29
                temp_m += 1
            if temp_m == 2 and self.y % 4 != 0 and temp_d > 28:
                temp_d=temp_d-28
                temp_m += 1
        self.d=temp_d
        self.m=temp_m
        print(f"New Date is: {self.d}.{self.m}.{self.y}")

    def addMonths(self):
        print("<<*** Inside addMonths Function ***>>")
        c = int(input("Enter Number of months to be added: "))
        temp_m=self.m+c
        temp_d=self.d
        while temp_m>12:
            if temp_m>12:
                temp_m=temp_m-12
                self.y+=1
            if temp_m in [4,6,9,11] and temp_d>30:
                temp_d=30
            if temp_m==2 and self.y%4==0 and temp_d > 29:
                temp_d=29
            if temp_m==2 and self.y%4!=0 and temp_d > 28:
                temp_d=28
        self.d=temp_d
        self.m=temp_m
        print(f"New Date is: {self.d}.{self.m}.{self.y}")

    def addYears(self):
        print("<<*** Inside addYears Function ***>>")
        c = int(input("Enter Number of months to be added: "))
        temp_y = self.y + c
        if temp_y%4!=0 and self.d>28:
            self.d=28
        self.y=temp_y
        print(f"New Date is: {self.d}.{self.m}.{self.y}")

obj=MyDate()
obj.addDays()
obj.addMonths()
obj.addYears()