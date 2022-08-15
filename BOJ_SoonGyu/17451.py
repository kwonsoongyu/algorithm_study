import sys
#17451
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
num = 0

speed = data[-1]
for i in range(N-2,-1,-1):
    if speed < data[i]:
        speed = data[i]
    else:
        if speed % data[i]:
            speed = (speed // data[i]+1) * data[i]

print(speed)
