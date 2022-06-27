import sys
#17219

input = sys.stdin.readline

N,M = map(int,input().split())
data = {}

for i in range(N):
    email, password = map(str,input().split())
    data[email] = password

for j in range(M):
    word = input().rstrip()
    print(data[word])
