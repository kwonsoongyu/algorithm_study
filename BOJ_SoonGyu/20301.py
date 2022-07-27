import sys
from collections import deque
#20301

input = sys.stdin.readline

N,K,M = map(int,input().split())

data = deque()
result = []
num = 0

for i in range(N):
    data.append(i+1)

while data:
    if (num // M) % 2 == 1:
        data.rotate(K)
        result.append(data.popleft())
    else:
        data.rotate(-(K-1))
        result.append(data.popleft())
    num += 1

for i in range(len(result)):
    print(result[i])
