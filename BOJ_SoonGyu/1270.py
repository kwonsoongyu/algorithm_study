import sys
from collections import Counter
#1270

input = sys.stdin.readline

N = int(input())

for i in range(N):
    data = []
    data = list(map(int,input().split()))
    num = data.pop(0)

    result = Counter(data).most_common()
    result.sort(key = lambda x:-x[1])

    if result[0][1] > num/2:
        print(result[0][0])
    else:
        print("SYJKGW")
