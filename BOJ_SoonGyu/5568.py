import sys
from itertools import permutations
#5568

input = sys.stdin.readline

N = int(input())
K = int(input())
data = []
result = set()

for i in range(N):
    num = input().rstrip()
    data.append(num)

for i in permutations(data,K):
    result.add(''.join(i))

print(len(result))

