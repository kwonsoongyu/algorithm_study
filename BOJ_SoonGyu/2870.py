import sys
#2870
input = sys.stdin.readline

N= int(input())
word=""
data=[]
result=[]
for i in range(N):
    data.append(input().rstrip())

    for j in range(len(data[i])):
        if data[i][j].isdigit():
            if data[i][j].isdigit():
                word += data[i][j]
            if j == len(data[i])-1 and data[i][j].isdigit():
                result.append(int(word))
                word=""
        else:
            if word:
                result.append(int(word))
                word=""
result.sort()

for i in range(len(result)):
    print(result[i])
