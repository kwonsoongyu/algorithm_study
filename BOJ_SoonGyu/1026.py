import sys
# 2217
input = sys.stdin.readline

result = 0

N = int(input())

A = list((map(int,input().split())))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse = True)

for i in range(N):
    result += A[i]*B[i]
print(result)
