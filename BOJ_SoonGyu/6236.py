import sys
#6236
input = sys.stdin.readline

N,M = map(int,input().split())

data = []
for i in range(N):
    data.append(int(input()))

start = max(data)
end = sum(data)
result = 0

while start <= end:
    mid = (start+end)//2
    sum = 0
    num = 1

    for i in range(len(data)):
        if sum+data[i] > mid:
            sum = data[i]
            num +=1
        else:
            sum += data[i]

    if num > M:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)
