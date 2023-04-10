def invmod(a):
    for i in range(0,26):
        if (i*a)%26 == 1:
            return i

def mod(n):
    while n<0:
        n+=26
    return n%26

ct = "pwuffogwchfdwiwej"
freq=[0]*26
for i in ct:
    freq[ord(i)-97]+=1
print("frequency matrix :",freq)
totalnonzeros=0
for i in freq:
    if i !=0:
        totalnonzeros+=1
print(totalnonzeros)
charsinorder=[]
for i in range(totalnonzeros):
    max = 0
    maxindex=0
    for j in range(26):
        if(freq[j]>max):
            max = freq[j]
            maxindex=j
    if max!=0:
        freq[maxindex]=0
        charsinorder.append(chr(maxindex+97))
print(charsinorder)
print(len(charsinorder)==totalnonzeros)
pt=""
for i in range(totalnonzeros):
    a=[1,3,5,7,9,11,15,17,19,21,23,25]
    b=[mod(ord(charsinorder[i])-97-4*ele) for ele in a]
    c=[mod(19*a[z]+b[z]) for z in range(12)]
    for j in range(totalnonzeros):
        if i!=j:
            flag = False
            matchat=0
            for k in range(12):
                if (ord(charsinorder[j]))-97==c[k]:
                    flag=True
                    matchat=k
                    break
            if flag == True:
                pt =""
                for  s in ct:
                    pt+=chr(mod((ord(s)-97-b[k])*invmod(a[k]))+97)
                print(pt)