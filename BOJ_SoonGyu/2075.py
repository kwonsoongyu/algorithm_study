import heapq
import sys

#2075
input = sys.stdin.readline

num = int(input())
result = []

for i in range(num):
    data = list(map(int,input().split()))

    if not result:
        for j in data:
            heapq.heappush(result, j)
    else:
        for j in data:
            if result[0]<j:
                heapq.heappush(result,j)
                heapq.heappop(result)

print(result[0])

