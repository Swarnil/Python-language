class MyDate:
    def __init__(self):
        self.d=int(input("Enter Date:"))
        self.m=int(input("Enter Month:"))
        self.y=int(input("Enter Year:"))
    def addDays(self):
        c=int(input("How many days you want to add:"))
        date=self.d+c
        mon=self.m
        year=self.y
        while date>31:
            if mon in[1,3,5,7,8,10] and date>31:
                mon=mon+1
                date=date-31
            if mon in[4,6,9,11] and date>30:
                mon=mon+1
                date=date-30
            if mon in[2] and year%4==0 and date>29:
                mon=mon+1
                date=date-29
            if mon in[2] and year%4!=0 and date>28:
                mon=mon+1
                date=date-28
            if mon in[12] and date>31:
                date=date-31
                year=year+1
                mon=1
        print("New Date is:{}/{}/{}".format(date,mon,year))


s1=MyDate()
s1.addDays()