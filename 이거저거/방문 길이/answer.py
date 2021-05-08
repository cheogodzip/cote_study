def solution(N, road, K):
    visited = set([1])
    temp = [(1, 0)]
    while temp:
        current = temp.pop()
        if current[1] == K:
            continue
        for r in road:
            if (current[0] in r[:2]) and (r[2] + current[1] <= K):
                visited.add(r[0])
                visited.add(r[1])
                if current[0] == r[0]:
                    temp.append((r[1], r[2] + current[1]))
                else:
                    temp.append((r[0], r[2] + current[1]))
                r = 0
        road = list(filter(lambda a: a != 0, road))

    print(visited)
    return len(visited)

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))