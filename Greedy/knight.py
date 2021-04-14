def solution(loc):
    answer = 0
    if ord(loc[0]) >= ord('c'):
        if int(loc[1]) > 1:
            answer += 1
        if int(loc[1]) < 8:
            answer += 1
    if ord(loc[0]) <= ord('f'):
        if int(loc[1]) > 1:
            answer += 1
        if int(loc[1]) < 8:
            answer += 1
    if int(loc[1]) >= 3:
        if ord(loc[0]) >= ord('b'):
            answer += 1
        if ord(loc[0]) <= ord('g'):
            answer += 1
    if int(loc[1]) <= 6:
        if ord(loc[0]) >= ord('b'):
            answer += 1
        if ord(loc[0]) <= ord('g'):
            answer += 1

    return answer
print(solution("c2"))
# 왕실의 기사