class student:
    def __init__(self):
        self.rollno = int(input("Enter the roll no.: "))
        self.name = input("Enter the name: ")
        self.marklist = []
        self.stream = input("Enter the stream in caps : ")
        
    def getMarks(self):
        for i in range(5):
            n = int(input("Enter the marks of subject {}: ".format(i+1)))
            self.marklist.append(n)
            
    def getStream(self):
        if self.stream == 'A':
            print("The stream is Arts.")
        elif self.stream == 'S':
            print("The stream is Science.")
        elif self.stream == 'C':
            print("The stream is Commers.")
        else:
            print("No stream was selected.")
            
    def Persentage(self):
        self.total = sum(self.marklist)
        self.p = self.total/5
        print("Persentage is : ", self.p)
        
    def gradeGen(self):
        for i in self.marklist:
            if i>=90:
                print("The Grade is AA")
            elif i>=80 and i<90:
                print("The Grade is A")
            elif i>=70 and i<80:
                print("The Grade is B")
            elif i>=60 and i<70:
                print("The Grade is C")
            elif i>=50 and i<60:
                print("The Grade is D")
            elif i>=40 and i<50:
                print("The Grade is E")
            elif i<40:
                print("The Grade is F")

                
obj = student()
obj.getMarks()
obj.getStream()
obj.Persentage()
obj.gradeGen()
