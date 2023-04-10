import math
import numpy as np
n,p,q = 7,3,41

def mod(x,n):
    while x<0 : 
        x+=n
    return x%n

def apply_poly_mod(h,q):
    for i in range(len(h)):
        h[i] = mod(h[i],q)
    return h
    
def poly_mod_powers(h):
    h = [ele for ele in reversed(h)]
    new_h=[]
    temp_h= []
    for ele in h:
        temp_h.append(ele)
        if(len(temp_h) == n):
            new_h.append(temp_h)
            temp_h = []
    while len(temp_h) == 0 or len(temp_h) == 7:
        temp_h.append(0)
    new_h.append(temp_h)
    h = [0]*n
    for ele in new_h:
        for i in range(len(ele)):
            h[i] += ele[i]
    h = [ele for ele in reversed(h)]
    return h

f = [1,0,-1,1,1,0,-1]
g = [1,0,1,0,-1,-1,0]
m = [-1,0,1,1,-1,1]
r = [1,-1,0,0,0,1,-1]
fp =[1,2,0,1,1,1,1]
fq =[8,26,31,21,40,2,37]

h = np.polymul(g,fq)
for i in range(len(h)):
    h[i] = mod(p*h[i],q)
h = poly_mod_powers(h)
h = apply_poly_mod(h,q)
print("h : ",h)


# encryption
e = np.polyadd(np.polymul(r,h),m)
e = poly_mod_powers(e)
e = apply_poly_mod(e,q)
print("e : ",e)


#decryption
a = np.polymul(f,e)
a = poly_mod_powers(a)
a = apply_poly_mod(a,q)
for i in range(len(a)):
    a[i] = a[i] - math.floor(q/2)
print(a)

m = np.polymul(fp,a)
m = poly_mod_powers(m)
m = apply_poly_mod(m,q)
for i in range(len(m)):
    m[i] = m[i] - math.floor(q/2)


m = apply_poly_mod(m,p)
# m = [ele for ele in reversed(m)]
for i in range(len(m)):
    m[i] = m[i] - math.floor(p/2)
m=np.poly1d(m)
print("m : \n",m)