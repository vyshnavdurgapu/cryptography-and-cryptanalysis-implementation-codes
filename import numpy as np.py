import numpy as np
k = 4
n = 7
P =[];S=[];G=[];Gd=[]

def print_matrix(M):
    for row in M:
        print(row)
    print()

def generate_key():
    global G,P,Gd,S
    
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
    
    print("\n ASSUMED GENERATOR MATRIX \n G = ");print_matrix(G)
    print("\n ASSUMED BASE MATRIX \n S = ");print_matrix(S)
    print("\n ASSUMED PERMUTATION MATRIX \n P = ");print_matrix(P)
    
    Gd = np.dot(np.dot(S,G),P).tolist()
    
    for i in range(k):
        for j in range(n):
            Gd[i][j] = Gd[i][j] % 2
    
    print("\n PUBLIC KEY \n  G\' = ");print_matrix(Gd)
    return Gd
    
def encrypt(x,GD):
    
    e = [0,0,0,0,1,0,0]
    GD = np.array(GD,dtype=int)
    x = np.array(x,dtype=int)
    y=[]
    t = np.dot(x,GD).tolist()
    for i in range(len(t)):
        t[i] = t[i] % 2

    for i in range(len(e)):
        val = ( e[i] + t[i] ) % 2
        y.append(val)
    return y

def decode(y):
    e1 = y[-1] ^ y[-3] ^ y[-5] ^ y[-7]
    e2 = y[-2] ^ y[-3] ^ y[-6] ^ y[-7]
    e3 = y[-4] ^ y[-5] ^ y[-6] ^ y[-7]
    e=str(e1)+str(e2)+str(e3)
    e = int(e,2) - 1
    if(y[e]==1):
        y[e]=0
    else:
        y[e]=1
    return y

def decrypt(y):
    global P
    P = np.array(P)
    Pinv = np.linalg.inv(P).tolist()
    for i in range(n):
        for j in range(n):
            Pinv[i][j] = int(Pinv[i][j]) 
    print("\n P Inverse \n ");print_matrix(Pinv)
    
    y1 = np.dot(y,Pinv).tolist()
    print("\n y1 \n",y1)
    x1 = decode(y1)
    print("\n x1 \n",x1)
    x0 = x1[:k]
    print("\n x0 \n",x0)
    Sinv = np.linalg.inv(S).tolist()
    
    for i in range(k):
        for j in range(k):
            Sinv[i][j] = int(Sinv[i][j]) % 2
    print("\n S Inverse ");print_matrix(Sinv)
    x = np.dot(x0,Sinv).tolist()
    return x
#MAIN
Gd = generate_key()
print("_"*25," ENCRYPTION","_"*25);print()
x = list(input(" Enter message : "))
y = encrypt(x,Gd)
print("\n ENCRYPTED MESSAGE --> ",y)
print();print("_"*25," DECRYPTION","_"*25);print()
x = decrypt(y)
print("\n DECRYPTED MESSAGE --> ",x)