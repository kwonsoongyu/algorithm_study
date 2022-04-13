import sys
#4796
input = sys.stdin.readline

num = 1

while True:
    L,P,V = map(int,input().split())
    sum = 0

    if L == 0 and P == 0 and V == 0:
        break

    A = V // P
    B = V % P

    if B >= L:
        sum = int(A*L+L)
    else:
        sum = int(A * L + B)
    print("Case %d: %d"%(num,sum))
    num += 1
