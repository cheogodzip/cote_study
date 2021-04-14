def solution(time):
    answer = 0
    # 3, 13, 23, 30-39, 43, 53 -> 15번/ 1분
    # 3, 13, 23, 30-39, 43, 53 -> 15번/ 1시간
    for i in range(0, time +1):
        if '3' in str(i):
            answer += 3600
        else:
            answer += (45*15) + (15*60)

    return answer

print(solution(5))

# 3이 들어간 시간 리턴 문제