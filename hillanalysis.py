import numpy as np

def invmod(a):
    for i in range(0,26):
        if (i*a)%26 == 1:
            return i

def mod(n):
    while n<0:
        n+=26
    return n%26

p ="july"
c="delw"
ct="asdadas"
pmatxiset = []

t=[]
i=0
t.append(list(p[4*i:4*(i)+2]))
t.append(list(p[4*i+2:4*(i)+2+2]))
pmatxiset=t
print(pmatxiset)
for i in range(len(pmatxiset)):
    for j in range(len(pmatxiset[i])):
        pmatxiset[i][j]=ord(pmatxiset[i][j])-ord('a')
print(pmatxiset)
cmatrix =[[ord(c[0])-ord('a'),ord(c[1])-ord('a')],[ord(c[2])-ord('a'),ord(c[3])-ord('a')]]
print(pmatxiset[0][0]*pmatxiset[1][1]-pmatxiset[0][1]*pmatxiset[1][0])
det = invmod(mod(pmatxiset[0][0]*pmatxiset[1][1]-pmatxiset[0][1]*pmatxiset[1][0]))
print(det)
pmatxisetinv = [
        [ mod(det*pmatxiset[1][1]) , mod(-pmatxiset[0][1]*det) ],
        [ mod(-pmatxiset[1][0]*det) , mod(det*pmatxiset[0][0]) ]
]

key=np.dot(pmatxisetinv,cmatrix)

cmatrixset = []
for i in range (0,int(len(c)/4)):
    t=[]
    t.append(list(ct[4*i:4*(i)+2]))
    t.append(list(ct[4*i+2:4*(i)+2+2]))
    cmatrixset.append(t)
print(cmatrixset)
for i in range(len(cmatrixset)):
    for j in range(len(cmatrixset[i])):
        for z in range(len(cmatrixset[i][j])):
            cmatrixset[i][j][z]=ord(cmatrixset[i][j][z])-ord('a')
print(cmatrixset)