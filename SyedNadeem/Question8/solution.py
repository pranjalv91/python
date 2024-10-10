A = [1, 3, 5]
B = [2, 4, 6]
C = []

temp = 0

for a in A:
    C.append(a)

for b in B:
    C.append(b)


for i in range(len(C)):
    for j in range(len(C)):
        if(C[i] < C[j]):
            temp = C[i]
            C[i] = C[j]
            C[j] = temp
print(C)