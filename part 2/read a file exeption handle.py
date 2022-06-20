try:
    s = open('lol.py','r')
    print(s.read())
    s.close()
except FileNotFoundError:
    print("!!!Exeption Caught!!!")
