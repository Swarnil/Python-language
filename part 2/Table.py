import numpy as np
s=np.arange(1,41).reshape(10,4)
print(s)
first=[]
g=s.reshape(1,-1)
for i in range(0,35,4):
    first.append(g[0,i:i+8])
print(np.array(first))
price=s[2:,3:4]
print(price)
