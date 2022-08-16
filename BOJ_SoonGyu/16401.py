import sys
#16401
input = sys.stdin.readline

M,N= map(int,input().split())

data = list(map(int,input().split()))

start = 0
end = max(data)
total = 0

while start <= end:
    mid = (start + end) // 2
    result = 0

    if mid == 0:
        result =0
        break

    for i in data:
        if i >= mid:
            result += (i//mid)

    if result >= M:
        total = mid
        start = mid + 1
    else:
        end = mid -1

print(total)
