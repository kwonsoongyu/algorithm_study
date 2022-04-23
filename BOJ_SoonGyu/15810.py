import sys
#15810
input = sys.stdin.readline

N,M = map(int,input().split())

data = list(map(int,input().split()))

start = 0
end = max(data)*M
num = 0
while start <= end:
    mid = (start+end)//2

    if sum([mid//n for n in data]) >= M:
        num = mid
        end = mid - 1
    else:
        start = mid + 1
print(num)


