import sys
from collections import deque
#2346

input = sys.stdin.readline

N = int(input())

numlist = deque(enumerate(map(int,input().split())))
idx = []
result = []

while numlist:
    result.append(numlist[0][0]+1)
    idx.append(numlist[0][1])
    numlist.popleft()

    if idx[-1] > 0:
        numlist.rotate(-(idx[-1]-1))
    else:
        numlist.rotate(-idx[-1])

for i in range(len(result)):
    print(result[i],end=" ")
