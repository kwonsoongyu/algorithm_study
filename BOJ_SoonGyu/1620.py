import sys
#1620
input = sys.stdin.readline

N,M = map(int,input().split())

data = []
quiz = []
for i in range(N):
    data.append(input().rstrip())

result = {data[i]:i+1 for i in range(N)}

for i in range(M):
    quiz.append(input().rstrip())

    if quiz[i].isdigit():
        print(data[int(quiz[i])-1])
    else:
        print(result.get(quiz[i]))
