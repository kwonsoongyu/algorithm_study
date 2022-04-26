import sys
import math
#2792
input = sys.stdin.readline

N,M = map(int,input().split())

data = []

for i in range(M):
    data.append(int(input()))

start = 1
end = max(data)
result = 0
num = 0

while start <= end:
    mid = (start + end) // 2
    num = 0
    for j in data:
        num += math.ceil(j/mid)

    if num > N:
        start = mid + 1
    else:
        result = mid
        end = mid -1

print(result)


