import sys
#20920

input = sys.stdin.readline

N,M = map(int,input().split())
data = {}

for i in range(N):
    word = input().rstrip()

    if len(word) >= M:
        if word in data:
            data[word] += 1
        else:
            data[word] = 1

result = sorted(data.items(), key = lambda x: (-x[1],-len(x[0]),x[0]))

for i in result:
    print(i[0])

