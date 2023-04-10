#ecc elgamal
def invmod (x,n):
    for i in range(0,n):
        if (i*x)%n==1:
            return i
def mod(x,n):
    while x<0:
        x=x+n
    return x%n    

def isvaldipoint(p):
    global ea,eb,z
    if p[1]**2%z== (p[0]**3+ea*p[0]+eb)%z:
        return True
    else:
        return False

def pointadd(a,b):
    global z , ea ,eb
    l=None
    if a[0]==b[0] and a[1]==b[1]:
        l= ((3*(a[0]**2)+ea)%z)*invmod(2*a[1],z)%z
    else:
        l= (mod(b[1]-a[1],z)*invmod(b[0]-a[0],z))%z
    # print(l)
    x3=mod(((l**2)-a[0]-b[0]),z)
    y3=mod(mod(l*(a[0]-x3),z)-a[1],z)
    return [x3,y3]

def pointmulti (n,e):
    if n==1:
        return e
    elif n==2:
        return pointadd(e,e)
    else :
        return pointadd(pointmulti(int(n/2),e),pointmulti(n-int(n/2),e))

ea=2
eb=3
z=67
d=4
e1=[2,22]
r=8
p =[24,26]

if not (isvaldipoint(p) and isvaldipoint(e1)):
    print('not valid points')
else:
    e2 = pointmulti(d,e1)
    print('e2: ',e2)

    #encyption
    c1 = pointmulti(r,e1)
    c2 = pointadd(p,pointmulti(r,e2))

    print('c1: ',c1)
    print('c2: ',c2)

    #decryption
    t = pointmulti(d,c1)
    t = [t[0],mod(-t[-1],z)]
    pt=pointadd(c2,t)
    print('pt: ',pt)