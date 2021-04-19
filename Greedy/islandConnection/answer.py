# 아직 못품 -> 정확성에서 틀림

def solution(n, costs):
    answer = 0
    connected = set()
    costs.sort(key = lambda temp:temp[2])
    print(costs)
    for cost in costs:
        print("실행")
        if (cost[0] in connected) and (cost[1] in connected):
            continue
        answer += cost[2]
        connected.add(cost[0])
        connected.add(cost[1])
        if len(connected) == n:
            break
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))