import sys
input = sys.stdin.readline
from collections import deque
#2477

K = int(input())

width = []
height = []
total = []
for i in range(6):
    dir, length = map(int,input().split())

    if dir == 1 or dir == 2:
        width.append(length)
        total.append(length)
    elif dir == 3 or dir == 4:
        height.append(length)
        total.append(length)

maxwidth = max(width) * max(height)

wididx = total.index(max(width))
heiidx = total.index(max(height))

minwidth = abs(total[wididx-1] - total[wididx-5])
minheight = abs(total[heiidx-1] - total[heiidx-5])
print((maxwidth - (minwidth*minheight)) * K)


