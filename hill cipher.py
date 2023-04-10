import numpy as np

def invmod(a):
    for i in range(0,26):
        if (i*a)%26 == 1:
            return i

def mod(n):
    while n<0:
        n+=26
    return n%26

# p = input()
p="july"
while len(p)%4!=0:
    p=p+'x'
print(p)
pmatxiset = []
for i in range (0,int(len(p)/4)):
    t=[]
    t.append(list(p[4*i:4*(i)+2]))
    t.append(list(p[4*i+2:4*(i)+2+2]))
    pmatxiset.append(t)
print(pmatxiset)
k =[[11,8],[3,7]]

# encryption 
for i in range(len(pmatxiset)):
    for j in range(len(pmatxiset[i])):
        for z in range(len(pmatxiset[i][j])):
            pmatxiset[i][j][z]=ord(pmatxiset[i][j][z])-ord('a')
print(pmatxiset)
cmatrixset=[]
c=""
for i in range(len(pmatxiset)):
    t=np.dot(pmatxiset[i],k)
    t=t.tolist()
    for ii in range(len(t)):
        for jj in range(len(t[ii])):
            t[ii][jj]=t[ii][jj]%26
            c+=chr(t[ii][jj]+ord('a'))
    cmatrixset.append(t)
print(cmatrixset)
print(c)

#decryption
det = invmod(k[0][0]*k[1][1]-k[0][1]*k[1][0])
kinv = [
        [ mod(det*k[1][1]) , mod(-k[0][1]*det) ],
        [ mod(-k[1][0]*det) , mod(det*k[0][0]) ] 
    ]
print(kinv)
pt=""
for i in range(len(cmatrixset)):
    t=np.dot(cmatrixset[i],kinv)
    t=t.tolist()
    for ii in range(len(t)):
        for jj in range(len(t[ii])):
            str=chr(t[ii][jj]%26+ord('a'))
            pt+=str
print(pt)