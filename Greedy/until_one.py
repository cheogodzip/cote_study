def solution(n, k):
    answer = 0
    while(n != 1):
        if n % k == 0:
            answer += 1
            n = n // k
        else:
            n -= 1
            answer += 1
    return answer

print(solution(25,3))

# 1이 될 때까지