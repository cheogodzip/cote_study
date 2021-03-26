visited = [] # 네트워크로 묶여진 컴퓨터
answer = 0 # 네트워크 수

def dfs(v, computers):
    visited.append(v) # 네트워크에 묶기
    for i in range(len(computers)):
        if i == v or computers[v][i] == 0:
            continue
        if i not in visited:
            dfs(i, computers)

def solution(n, computers):
    global answer
    for i in range(n):
        if i not in visited:
            dfs(i, computers)
            answer += 1

    return answer


print(solution(5, [[1, 1, 1,0,0], [1, 1, 0,0,0], [1, 0, 1, 0, 1], [0,0,0,1,0],[0,0,1,0,1]]))