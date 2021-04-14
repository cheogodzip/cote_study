def solution(size, arr):
    loc = [1,1]
    for i in arr:
        if i == 'R':
            if loc[1] == size:
                continue
            loc[1] += 1
        elif i == 'L':
            if loc[1] == 1:
                continue
            loc[1] -= 1
        elif i == 'U':
            if loc[0] == 1:
                continue
            loc[0] -= 1
        elif i == 'D':
            if loc[0] == size:
                continue
            loc[0] += 1
    print(loc)



solution(5,['R','R','R','U','D','D'])

# 상하좌우 문제