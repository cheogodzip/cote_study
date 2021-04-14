def solution(n, arr):
    answer = 0
    arr.sort()
    m = 0

    for i in arr:
        m += 1
        if i <= m:
            answer += 1
            m = 0

    return answer

print(solution(5, [2,3,1,2,2]))

# 모험가 길드