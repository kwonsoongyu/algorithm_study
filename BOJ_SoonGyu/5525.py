import sys
#5525
input = sys.stdin.readline

N = int(input())
idx = 0
count= 0
sum = 0
num = int(input())
word = str(input().rstrip())

while idx < num-1:
    if word[idx:idx+3] == 'IOI':
        count += 1
        idx += 2

        if count == N:
            sum += 1
            count -= 1
    else:
        idx += 1
        count = 0
print(sum)
