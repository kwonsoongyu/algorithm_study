import sys
from collections import deque
#18115

input = sys.stdin.readline

N = int(input())
result = []
data = deque()

result = list(map(int,input().split()))
result.reverse()

for i in range(N):
    if result[i] == 1:
        data.appendleft(i+1)
    elif result[i] == 2:
        data.insert(1,i+1)
    else:
        data.append(i+1)

for i in data:
    print(i,end=" ")



