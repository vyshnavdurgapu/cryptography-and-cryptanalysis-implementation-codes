import numpy as np
import math

def invmod(a):
    print(a)
    for i in range(26):
        if i*a%26==1:
            return i
def mod(a):
    while a<0:
        a+=26
    return a%26

def matrixinv(m):
    minv = np.linalg.inv(m).tolist()
    det = np.linalg.det(m)
    det=round(det)
    print(det)
    for i in range(len(minv)):
        for j in range(len(minv[i])):
            minv[i][j]*=det
            minv[i][j]=round(minv[i][j])
            minv[i][j]=mod(minv[i][j])
    adj=minv
    detinv=invmod(det)
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            adj[i][j]*=detinv
            adj[i][j]=adj[i][j]%26
    return adj


# pt = "iampersonabc"
pt ="july"
matlen= 2

while len(pt)%matlen!=0:
    pt+='x'
# print(pt)
pta = [ord(e)-97 for e in pt]
# print(pta)
ptm=[]
for i in range(0,len(pt)//matlen):
    ptm.append(pta[matlen*i:matlen*i+matlen])
print(ptm)

k =[[11,8],[3,7]]
print(matrixinv(k))
# print(k)

#encryption
ctm = []
for m in ptm:
    t=np.dot(m,k).tolist()
    t = [e%26 for e in t]
    ctm.append(t)
print(ctm)

ct=""
for i in range(len(ctm)):
    for j in range(len(ctm[i])):
        ct+=chr(ctm[i][j]+ord('a'))
print(ct)

#decryption
kinv=matrixinv(k)
print(kinv)
pt=""
ptm=[]
for m in ctm:
    t=np.dot(m,kinv).tolist()
    t = [e%26 for e in t]
    ptm.append(t)
print(ptm)

for i in range(len(ptm)):
    for j in range(len(ptm[i])):
        pt+=chr(ptm[i][j]+ord('a'))
print(pt)