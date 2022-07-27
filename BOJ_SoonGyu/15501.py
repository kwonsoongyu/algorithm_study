import sys
from collections import deque
#15501

input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
result = list(map(int,input().split()))

#순방향
resultidx = result.index(data[0])
forward = result[resultidx:]+result[:resultidx]

#역방향
result = result[::-1]
resultidx = result.index(data[0])
backword = result[resultidx:]+result[:resultidx]

if data == forward or data == backword:
    print("good puzzle")
else:
    print("bad puzzle")
