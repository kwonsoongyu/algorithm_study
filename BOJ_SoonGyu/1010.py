import sys
import math

#1010
input = sys.stdin.readline

T = int(input())
data = []
for i in range(T):
    N,M = map(int,input().split())

    if N == M:
        print("1")
    else:
        sum = math.factorial(M)
        div = math.factorial(M-N) * math.factorial(N)
        print(sum//div)
