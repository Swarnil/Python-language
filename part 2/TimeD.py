import datetime


class myDate:

    def addDays(self, n):
        if n == 0:
            n = int(input("Enter days to add: "))

        newDate = self.theDate + datetime.timedelta(days=n)
        print("New date:", newDate.strftime("%d-%m-%Y"))

    def addMonths(self):
        m = int(input("Enter months to add: "))

        if m > 12:  # 14
            y = m // 12  # 1
            m = m % 12  # 2
            print("New date:", datetime.date(y + self.year, m + self.month, d).strftime("%d-%m-%Y"))
        else:

            print("New date:", datetime.date(self.year, m + self.month, d).strftime("%d-%m-%Y"))

    def addYears(self):
        y = int(input("Enter years to add: "))
        print("New date:", datetime.date(y + self.year, m, d).strftime("%d-%m-%Y"))

    def weekday(self):
        day = self.theDate.weekday()
        if day == 0:
            print("It is a MONDAY")
        elif day == 1:
            print("It is a TUESDAY")
        elif day == 2:
            print("It is a WEDNESDAY")
        elif day == 3:
            print("It is a THURSDAY")
        elif day == 4:
            print("It is a FRIDAY")
        elif day == 5:
            print("It is a SATURDAY")
        else:
            print("It is a SUNDAY")

    def diffDates(self):
        date1 = datetime.date(d1.year, d1.month, d1.day)
        date2 = datetime.date(d2.year, d2.month, d2.day)
        delta = date2 - date1
        day = delta.days
        years = day // 365
        day = day - years
        months = day // 30
        day = day - (months * 30)
        print(years, "years,", months, "months and", day, "days")

    def futureDate(self):
        d, m, y = map(int, input("Enter how many days, months and years you want to add: ").split())
        d = d + (m * 30.417) + (y * 365.2425)
        d1.addDays(d)

    def pastDate(self):
        d, m, y = map(int, input("Enter how many days, months and years you want to subtract: ").split())
        d = -(d + (m * 30.417) + (y * 365.2425))
        d1.addDays(d)

    def __init__(self, d, m, y):
        self.theDate = datetime.date(y, m, d)
        # makes the date out of input
        self.year = y
        self.month = m
        self.day = d


choice = int(input(
    "Choose the operation you want to perform:\n\n1.Add days to a date\n2.Add months to a date\n3.Add years to a date\n4.Return the weekday\n5.Find difference of two dates\n6.Find a future date\n7.Find a past date\n\nNow enter your choice: "))

if choice == 1:
    d, m, y = map(int, input("Enter any date: ").replace("/", "-").split("-"))
    d1 = myDate(d, m, y)  # calling the constructor
    d1.addDays(0)

elif choice == 2:
    d, m, y = map(int, input("Enter any date: ").replace("/", "-").split("-"))
    d1 = myDate(d, m, y)  # calling the constructor
    d1.addMonths()

elif choice == 3:
    d, m, y = map(int, input("Enter any date: ").replace("/", "-").split("-"))
    d1 = myDate(d, m, y)  # calling the constructor
    d1.addYears()

elif choice == 4:
    d, m, y = map(int, input("Enter any date: ").replace("/", "-").split("-"))
    d1 = myDate(d, m, y)  # calling the constructor
    d1.weekday()

elif choice == 5:
    d, m, y = map(int, input("Enter first date: ").replace("/", "-").split("-"))
    d1 = myDate(d, m, y)
    d, m, y = map(int, input("Enter second date: ").replace("/", "-").split("-"))
    d2 = myDate(d, m, y)
    d1.diffDates()

elif choice == 6:
    d, m, y = map(int, input("Enter any date: ").replace("/", "-").split("-"))
    d1 = myDate(d, m, y)
    d1.futureDate()

elif choice == 7:
    d, m, y = map(int, input("Enter any date: ").replace("/", "-").split("-"))
    d1 = myDate(d, m, y)
    d1.pastDate()

else:
    print("Invalid choice")
