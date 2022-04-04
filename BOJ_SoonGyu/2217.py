import sys
# 2217
input = sys.stdin.readline

N = int(input())
data = []
max = 0
for i in range(N):
    weight = int(input())
    data.append(weight)

data.sort()
num = N

for i in range(N):
    if max < data[i]*num:
        max = data[i]*num
    num -= 1

print(max)
