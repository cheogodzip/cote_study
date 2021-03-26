def dfs(x,y,n,m,graph):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] == 1
        dfs(x-1,y,n,m,graph)
        dfs(x,y-1,n,m,graph)
        dfs(x+1,y,n,m,graph)
        dfs(x,y+1,n,m,graph)
        return True
    return False

graph = []
answer = 0
for i in range(4):
    graph.append(list(map(int,input().split())))
for i in range(4):
    for j in range(5):
        if dfs(i,j,4,5,graph) == True:
            answer += 1

print(answer)