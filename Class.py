zero=0
positive=0
negative=0
n=int(input("Enter Terms:"))
for i in range(1,n+1,1):
        g=int(input("Enter Number:"))
        if g==0:
            zero=zero+1
        elif g>0:
            positive=positive+1
        elif g<0:
            negative=negative+1
print("Total Positive ",positive)
print("Total Negative: ",negative)
print("Total Zero: ",zero)