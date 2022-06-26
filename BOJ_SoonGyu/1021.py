import sys
from collections import deque
#1021

input = sys.stdin.readline

A,B = map(int,input().split())
data = list(map(int,input().split()))

result = deque()

for i in range(1,A+1):
    result.append(i)

count = 0
for i in data:
    while True:
        if i == result[0]:
            result.popleft()
            break
        else:
            if result.index(i) < len(result)/2:
                while result[0] != i:
                    result.append(result.popleft())
                    count += 1
            else:
                while result[0] != i:
                    result.appendleft(result.pop())
                    count += 1
print(count)
