import numpy as np
G = [ [1, 0, 0, 0, 1, 1, 0],
      [0, 1, 0, 0, 1, 0, 1],
      [0, 0, 1, 0, 0, 1, 1],
      [0, 0, 0, 1, 1, 1, 1] ]

S = [ [1, 1, 0, 1],
      [1, 0, 0, 1],
      [0, 1, 1, 1],
      [1, 1, 0, 0] ]
    
P = [ [0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1, 0, 0] ]

g1 = np.dot(S,G)
g1 = np.dot(g1,P)

for i in range(0,len(g1)):
    for j in range(0,len(g1[i])):
        g1[i][j]=g1[i][j]%2
# print(g1)

m=[1,0,1,1]

#encryption
e=[0,0,0,0,1,0,0]

y = np.dot(m,g1)

for i in range(0,len(e)):
    y[i]+=e[i]
    y[i]=y[i]%2

#decryption
pinv = np.linalg.inv(P).tolist()
for i in range(7):
    for j in range(7):
        pinv[i][j] = int(pinv[i][j]) % 2

y1 = np.dot(y,pinv)

e1 = y1[-1] ^ y1[-3] ^ y1[-5] ^ y1[-7]
e2 = y1[-2] ^ y1[-3] ^ y1[-6] ^ y1[-7]
e3 = y1[-4] ^ y1[-5] ^ y1[-6] ^ y1[-7]

e=str(e1)+str(e2)+str(e3)
e = int(e,2) - 1

if(y1[e]==1):
    y1[e]=0
else:
    y1[e]=1

x0=y1[:4]

sinv = np.linalg.inv(S).tolist()
for i in range(4):
        for j in range(4):
            sinv[i][j] = int(sinv[i][j]) % 2

x = np.dot(x0,sinv).tolist()
for i in range (len(x)):
    x[i]=x[i]%2
print(x)