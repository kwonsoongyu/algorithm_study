import sys
# 2847
input = sys.stdin.readline

N = int(input())
data = []
level = 0

for i in range(N):
    num = int(input())
    data.append(num)

max= data[-1]

for i in data[-2::-1]:
    if i > max:
          level += i-max+1
          max -= 1
    elif i < max:
        max = i
    elif i == max:
        level += 1
        max -= 1
    else:
        max -= 1

print(level)
