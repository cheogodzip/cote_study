# 4 * 5 얼음 틀 입력 0이 빈 곳, 1은 틀
# 만들 수 있는 아이스크림 개수
# bfs 사용
from collections import deque

answer = 0
n, m = list(map(int, input().split()))
frame = []
for _ in range(n):
    frame.append(list(input()))

for x in range(n):
    for y in range(m):
        if frame[x][y] == '1':
            continue
        frame[x][y] = '1'
        answer += 1
        queue = deque([[x,y]])
        while queue:
            tx, ty = queue.popleft()
            if tx != 0:
                if frame[tx-1][ty] == '0':
                    frame[tx-1][ty] = '1'
                    queue.append([tx-1,ty])
            if tx != (n-1) :
                if frame[tx+1][ty] == '0':
                    frame[tx+1][ty] = '1'
                    queue.append([tx + 1, ty])
            if y!= 0:
                if frame[tx][ty-1] == '0':
                    frame[tx][ty-1] = '1'
                    queue.append([tx, ty-1])
            if ty != (m-1):
                if frame[tx][ty+1] == '0':
                    frame[tx][ty+1] = '1'
                    queue.append([tx, ty + 1])


print(answer)
