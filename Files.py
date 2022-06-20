# f1=open('test.py','w')
# f1.write("Hi")
# f1.write("Gopal")
# f1.writelines("Hello")
# f1.writelines("World")

# f1.close()
f1=open('test.py','r')
f1.close()

f1=open('test.py','a')
f1.write("MCA")
f1.close()

f1=open('test.py','r')
print(f1.read())
f1.close()



