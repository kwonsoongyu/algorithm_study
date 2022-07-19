import sys
from itertools import combinations
#23057

input = sys.stdin.readline

N = int(input())

data = list(map(int,input().split()))

datasum = sum(data)

num = set()

for i in range(1, N+1):
    for j in combinations(data,i):
        print(j)
        num.add(sum(j))

print(datasum-len(num))


