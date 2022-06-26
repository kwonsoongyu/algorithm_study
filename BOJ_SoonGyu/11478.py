import sys

#11478

input = sys.stdin.readline

word = input().rstrip()
data= []
result = set()
for i in range(len(word)):
    data.append(word[i])

for i in range(len(word)):
    for j in range(i+1,len(word)+1):
        temp = data[i:j]
        result.add("".join(temp))
print(len(result))

