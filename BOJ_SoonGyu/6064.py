import sys
#6064

def result(m,n,x,y):
    k = x
    while k<=m*n:
        if (k-x)%m == 0 and (k-y)%n == 0:
            return k
        k += m
    return -1

T = int(input())

for i in range(T):
    M,N,X,Y = map(int,input().split())

    print(result(M,N,X,Y))
