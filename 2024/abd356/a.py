N,L,R = list(map(int, input().split()))

array1_L=[]
arrayL_R=[]
arrayR_N=[]

for i in range(1,L):
    array1_L.append(i)

for i in range(L,R+1):
    arrayL_R.append(i)

for i in range(R+1,N+1):
    arrayR_N.append(i)

arrayL_R.reverse()

array = array1_L + arrayL_R + arrayR_N

print(" ".join(map(str,array)))
