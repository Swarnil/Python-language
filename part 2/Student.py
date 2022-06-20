# class Student:
#     def __init__(self):
#         self.rollNum=int(input("Enter Roll : "))
#         self.name=input("Enter Name: ")
#         self.marklist=[]
#         self.stream=input(f"Enter Stream for {self.name}: ")
#     def setMarks(self):
#         print(f"*** Enter Five Marks for {self.name} ***")
#         for i in range(5):
#             self.g=int(input(f"Enter Marks For Subject[{i+1}]:"))
#             self.marklist.append(self.g)
#     def getStream(self):
#         if self.stream=='A':
#             print(f"{self.name}'s Steam is Atrs")
#         if self.stream=='C':
#             print(f"{self.name}'s Steam is Commerce")
#         if self.stream=='S':
#             print(f"{self.name}'s Steam is Science")
#
#     def percentage(self):
#         self.s=sum(self.marklist)
#         print(f"Percentage for {self.name} is {self.s/5}% ")
#
#     def gradeGen(self):
#         print(f"*** Grade For {self.name} ***")
#         for i in range(5):
#             if self.marklist[i]>=90:
#                 print(f"Subject{i+1}: A")
#             if self.marklist[i] <90 and self.marklist[i] >=80:
#                 print(f"Subject{i+1}: B")
#             if self.marklist[i] <80 and self.marklist[i]>=65:
#                 print(f"Subject{i+1}: C")
#             if self.marklist[i] <65 and  self.marklist[i]>=40:
#                 print(f"Subject{i+1}: D")
#             if self.marklist[i] <40:
#                 print(f"Subject{i+1}: E")
# obj=Student()
# obj.setMarks()
# obj.getStream()
# obj.percentage()
# obj.gradeGen()

class Item:
    def __init__(self):
        self.name=input("Enter Item Name: ")
        self.price=int(input("Enter Item Price: "))
        self.quantity=int(input("Enter Item Quantity: "))
    def Purchase(self):
        self.p=int(input("Enter Number Of Items To Be Purchased: "))
        while self.p>self.quantity:
            print(f"Sorry! {self.p} Items Is Not Available ")
            self.p = int(input("Enter Number Of Items To Be Purchased: "))
        else:
            self.quantity=self.quantity-self.p
            print(f"*** {self.p} Items Sold ***")
    def increaseStock(self):
        self.inc = int(input("Enter Number Of Items To Be Increased: "))
        self.quantity = self.quantity +self.inc
    def Display(self):
        print(" *** Item Details ***")
        print(f"Item Name: {self.name}")
        print(f"Item Price: {self.price}")
        print(f"Updated Quantity: {self.quantity}")
obj=Item()
obj.Purchase()
obj.increaseStock()
obj.Display()