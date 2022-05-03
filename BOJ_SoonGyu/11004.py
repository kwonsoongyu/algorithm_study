import sys
#11004
input = sys.stdin.readline

N,M = map(int,input().split())
result = list(map(int,input().split()))

result.sort()

print(result[M-1])
