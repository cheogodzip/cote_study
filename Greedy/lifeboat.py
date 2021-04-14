# 최대 2명만 탈 수 있는 보트

def solution(people, limit):
    answer = 0
    people.sort()
    while len(people) <= 1:
        if limit >= (people[-1] + people[0]):
            del people[0]
        people.pop()
        answer += 1
    if len(people) == 1:
        answer += 1
    return answer


print(solution([70,50,80,50], 100))