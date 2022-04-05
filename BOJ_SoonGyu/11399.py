import sys
# 11399
input = sys.stdin.readline

N = int(input())
sum = 0
time = list(map(int,input().split()))

time.sort()

for i in range(1,len(time)):
    time[i] = time[i]+time[i-1]

for i in range(len(time)):
    sum += time[i]

print(sum)
