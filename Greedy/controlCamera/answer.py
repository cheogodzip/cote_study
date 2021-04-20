def solution(routes):
    answer = 1
    routes.sort() # 구간 시작이 가까운 것들끼리 비교하기 위해
    path = routes.pop(0)
    while routes:
        temp = routes.pop(0)
        if path[0] <= temp[0] <= path[1]:
            path[0] = temp[0]
            path[1] = path[1] if path[1] < temp[1] else temp[1]
        else:
            answer += 1
            path = temp


    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]	))