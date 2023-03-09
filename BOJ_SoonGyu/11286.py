import heapq
import sys
from heapq import heapify
#11286
input = sys.stdin.readline

N = int(input())

h = []


for i in range(N):
    num = int(input())

    if num != 0:
        if num < 0:
            heapq.heappush(h,(-num,num))
        else:
            heapq.heappush(h,(num,num))
    else:
        if h:
            result = heapq.heappop(h)[1]
            print(result)
        else:
            print("0")
