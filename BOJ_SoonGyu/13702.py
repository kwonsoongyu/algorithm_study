import sys
#13702
input = sys.stdin.readline

N,K = map(int,input().split())
data = []
num = 0

for i in range(N):
    data.append(int(input()))

data.sort()

start = 1
end = data[-1]

while start<=end: # 이분탐색
    mid = (start+end)//2
    num = 0

    for i in data:
        num += i//mid

    if num < K:
        end = mid - 1
    else:
        start = mid + 1

print(end)


