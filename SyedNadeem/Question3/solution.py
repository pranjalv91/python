A = [3, 3, 4, 4, 4, 5, 5, 5, 2]

maxcount = 0
element_with_maxFrequency = 0

for a in range(len(A)):
    count = 0
    for b in range(len(A)):
        if A[a] == A[b]:
            count = count + 1

if (count > maxcount):
    maxcount = count
    element_with_maxFrequency = A[b]
    print(maxcount)