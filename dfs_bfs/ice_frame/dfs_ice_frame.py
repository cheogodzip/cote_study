# 4 * 5 얼음 틀 입력 0이 빈 곳, 1은 틀
# 만들 수 있는 아이스크림 개수
# dfs 사용

def dfs(tx, ty):
    if tx < 0 or tx >= n or ty < 0 or ty >= m:
        return False
    if frame[tx][ty] == '0':
        frame[tx][ty] = '1'
        dfs(tx - 1, ty)
        dfs(tx + 1, ty)
        dfs(tx, ty - 1)
        dfs(tx, ty + 1)
        return True
    return False

answer = 0
n, m = map(int, input().split())
frame = []
for _ in range(n):
    frame.append(list(input()))

for x in range(n):
    for y in range(m):
        if dfs(x,y) == True:
            answer += 1
print(answer)
