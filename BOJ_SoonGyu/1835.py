import sys
from collections import deque
#1835

input = sys.stdin.readline

N = int(input())
data = deque()

data.append(N)

for i in range(N-1,0,-1):
    data.appendleft(i)

    for j in range(i):
        num = data.pop()
        data.appendleft(num)

print(*data)
import sys
from collections import deque
#1835

input = sys.stdin.readline

N = int(input())
data = deque()

data.append(N)

for i in range(N-1,0,-1):
    data.appendleft(i)

    for j in range(i):
        num = data.pop()
        data.appendleft(num)

print(*data)
