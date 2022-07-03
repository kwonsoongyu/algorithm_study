import sys
#2002

input = sys.stdin.readline

N = int(input())
result = 0

first = {}
last = []

for i in range(N):
    car = input().rstrip()
    first[car] = i

for i in range(N):
    car = input().rstrip()
    last.append(car)

for i in range(N-1):
    for j in range(i+1,N):
        if first[last[i]] > first[last[j]]:
            result += 1
            break
print(result)



