global answer
answer = 0

def dfs(numbers, v, target):
    global answer
    v += 1
    if len(numbers) == v:
        if target == 0:
            answer += 1

        return
    dfs(numbers, v, target + numbers[v])
    dfs(numbers, v, target - numbers[v])

def solution(numbers, target):
    dfs(numbers,-1, target)
    return answer

print(solution([1,1,1,1,1], 3))