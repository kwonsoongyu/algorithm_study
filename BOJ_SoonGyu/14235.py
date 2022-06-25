import heapq
import sys

#14235
input = sys.stdin.readline

num = int(input())
result = []

for i in range(num):
    number = list(map(int,input().split()))

    if(number[0] == 0):
        if result:
            print(-heapq.heappop(result))
        else:
            print("-1")
    else:
        for j in range(1,len(number)):
            heapq.heappush(result,-number[j])

