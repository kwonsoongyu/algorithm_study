import sys
from collections import deque
#12873
input = sys.stdin.readline

N = int(input())

data = deque()

for i in range(N):
    data.append(i+1)

data.popleft()

for i in range(2,N):
    data.rotate(-(i**3))
    data.pop()

if data:
    print(*data)
else:
    print("1")
