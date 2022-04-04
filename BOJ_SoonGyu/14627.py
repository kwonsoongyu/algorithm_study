import sys
#17266
input = sys.stdin.readline

S,C = map(int,input().split())
data = []
num = 0

for i in range(S):
    data.append(int(input()))

data.sort()

start = 1
end = data[-1]

while start<=end:
    mid = (start+end)//2
    num = 0

    for i in data:
        num += i//mid

    if num < C:
        end = mid - 1
    else:
        start = mid + 1

print(sum(data)-(C*end))
