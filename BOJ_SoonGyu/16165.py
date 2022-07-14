import sys
#16165

input = sys.stdin.readline

N,M = map(int,input().split())
data = {}
for i in range(N):
    group = []
    word = str(input().rstrip())
    member = int(input())
    for j in range(member):
        name = str(input().rstrip())
        group.append(name)
    data[word] = group


for i in range(M):
    question = str(input().rstrip())
    num = int(input())

    if num == 1:
        for keys, value in data.items():
            for j in range(len(value)):
                if question == value[j]:
                    print(keys)
                    break
    else:
        if question in data:
            result = list(data[question])
            result.sort()
            for t in result:
                print(t)
