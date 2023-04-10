def invmod(a):
    for i in range(0,26):
        if (i*a)%26 == 1:
            return i

def mod(n):
    while n<0:
        n+=26
    return n%26

ct = "pwuffogwchfdwiwej"
freq =[0]*26
for s in ct :
    freq[ord(s)-ord('a')]+=1
print(freq)
totnonzeros =0
for x in freq:
    if x!=0:
        totnonzeros+=1
print(totnonzeros)
charsinorder =[]
for i in range(0,totnonzeros):
    max = 0
    maxindex=0
    for j in range(0,26):
        if freq[j]>max:
            max = freq[j]
            maxindex=j
    if max!=0:
        freq[maxindex]=0
        charsinorder.append(chr(maxindex+ord('a')))
print(len(charsinorder))
print(charsinorder)

pt =""
for i in range(0,totnonzeros):
    a=[1,3,5,7,9,11,15,17,19,21,23,25]
    b=[]
    for  e in range(12):
        b.append(ord(charsinorder[i])-ord('a')-4*a[e])
    b=[mod(e) for e in b]
    c=[a[e]*19+b[e] for e in range(12)]
    c=[mod(e) for e in c]
    for k in range(12):
        print(a[k]," ",b[k]," ",c[k])
    for j in range(totnonzeros):
        if i!=j:
            flag=False
            matchat=0
            for p in range (12):
                if c[p]==ord(charsinorder[j])-ord('a'):
                    flag=True
                    matchat=p
                    break
            if flag==True:
                ainv = invmod(a[p])
                for l in ct:
                    pt+= chr(mod(mod(mod(ord(l)-ord('a')-b[matchat]))*ainv)+ord('a'))
                print(pt)
                pt=""