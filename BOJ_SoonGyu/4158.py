import sys
#13702
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
    arrayN = []
    arrayM = []
    sum = 0

    for i in range(N):
        arrayN.append(int(input()))

    for i in range(M):
        arrayM.append(int(input()))
    arrayM.sort()
    idxN,idxM = 0,0

    while True:
        if(idxN == N or idxM == M):
            break
        if(arrayN[idxN]<arrayM[idxM]):
            idxN += 1
        elif(arrayN[idxN]>arrayM[idxM]):
            idxM += 1
        elif(arrayN[idxN]==arrayM[idxM]):
            idxN += 1
            idxM += 1
            sum += 1
    print(sum)

