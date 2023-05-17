import sys
input = sys.stdin.readline
#14719

H,W = map(int,input().split())

row = list(map(int,input().split()))

result = 0

for i in range(1,W-1):
    left_max = max(row[:i])
    right_max = max(row[i+1:])

    compare = min(left_max,right_max)

    if row[i] < compare:
        result += compare - row[i]

print(result)
