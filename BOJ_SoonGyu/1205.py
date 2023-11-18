import sys

input = sys.stdin.readline

N,score,P = map(int,input().split())
result = 1

if N == 0:
    print("1")
else:
    test = list(map(int, input().split()))
    num = test[0]
    if test[-1] >= score and N == P:
        print("-1")
    else:
        result = N + 1
        for i in range(N):
            if test[i] <= score:
                result = i + 1
                break
        print(result)



