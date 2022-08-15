import sys
#25325

input = sys.stdin.readline

N = int(input())

data = list(map(str,input().split()))
result = {}

for i in data:
    result[i] = 0

for i in range(len(data)):
    word = list(map(str,input().split()))
    for j in range(len(word)):
        if word[j] in result:
            result[word[j]] += 1

result = sorted(result.items(), key = lambda item:(-item[1],item[0]))

for i in range(N):
    print(result[i][0],result[i][1])
