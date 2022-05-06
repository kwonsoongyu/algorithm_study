import sys
#11659
input = sys.stdin.readline

N,M = map(int,input().split())

data = list(map(int,input().split()))
num_sum = [0 for i in range(N)]

for i in range(N):
    if i == 0:
        num_sum[i] = data[i]
    else:
        num_sum[i] = data[i]+num_sum[i-1]

for t in range(M):
    i,j = map(int,input().split())
    sum = 0
    if i == 1:
        print(num_sum[j-1])
    else:
        print(num_sum[j-1]-num_sum[i-2])

