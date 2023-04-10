import math
n = 187
base=[2,3,5,7,11]
pairs=[]
for i in range (int(n**0.5),n):
    for j in base:
        lhs = (i**2)%n
        rhs = (j**2)%n
        if lhs ==rhs :
            pairs.append([i,j])
            
new = []
for i in range(len(pairs)):
    d = math.gcd(pairs[i][0]-pairs[i][1],n)
    if d!=1 and d!=n:
        if d not in new:
            new.append(d)
print(new)
