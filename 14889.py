import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#14889

N = int(input())
visited = [False for _ in range(N)]
graph = []
min_num = 100000000000

for i in range(N):
    graph.append(list(map(int,input().split())))

def dfs(depth,idx):
    global min_num
    if depth == N//2:
        front = 0
        end = 0
        for j in range(N):
            for k in range(N):
                if visited[j] and visited[k]:
                    front += graph[j][k]
                elif not visited[j] and not visited[k]:
                    end += graph[j][k]

        min_num = min(min_num,abs(front-end))
        return

    for t in range(idx,N):
        if not visited[t]:
            visited[t] = True
            print(visited)
            dfs(depth+1,t+1)
            visited[t] = False

dfs(0,0)
print(min_num)
