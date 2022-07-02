import sys
#2304

input = sys.stdin.readline

N = int(input())
data = []
sum = 0
maxH = 1
maxL = 0
for i in range(N):
    start, height = map(int,input().split())
    data.append([start,height])

    if maxL < start:
        maxL = start
    if maxH < height:
        maxH = height
        maxindex = start

result = [0] * (maxL+1)
for l,h in data:
    result[l] = h

temp = 0
for i in range(maxindex+1):
    if result[i] > temp:
        temp = result[i]
    sum += temp

temp = 0
for i in range(maxL, maxindex, -1):
    if result[i] > temp:
        temp = result[i]
    sum += temp

print(sum)





