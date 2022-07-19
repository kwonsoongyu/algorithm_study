import sys
#14425

input = sys.stdin.readline

N,M = map(int,input().split())
sum = 0
data = set()
for i in range(N):
    word = str(input().rstrip())
    data.add(word)

for i in range(M):
    word = str(input().rstrip())

    if word in data:
        sum += 1

print(sum)
