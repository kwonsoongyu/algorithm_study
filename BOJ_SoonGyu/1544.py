import sys
from collections import deque
#1544

input = sys.stdin.readline

N = int(input())
data = []

for i in range(N):
    word = str(input().rstrip())
    data.append(word)

for i in range(N):
    result = deque(data[i])
    while True:
        result.append(result.popleft())
        word = "".join(result)

        if word == data[i]:
            break

        if word in data:
            idx = data.index(word)
            data.pop(idx)
            data.insert(idx,data[i])

data2 = set(data)
print(len(data2))

