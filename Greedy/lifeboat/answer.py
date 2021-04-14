# 효율성 1번에서 걸림. -> 큐로 구현하니까 통과함
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while len(people) > 1:
        # 제일 가벼운 사람의 무게가 무게 제한의 절반보다 크면 한사람씩 밖에 못탄다.
        if people[0] > limit/2:
            answer += len(people)
            people = []
            break
        # 제일 무거운 사람의 무게가 무게 제한의 절반보다 이하면 모두 두사람씩 태울 수 있다.
        elif people[-1] <= limit/2:
            answer += len(people)//2 + len(people)%2
            people = []
            break

        # 2명이 최대이므로, 제일 가벼운 사람과 무거운 사람을 태운다.
        # 그렇지 못하면 제일 무거운 사람 한명만 태운다.
        if limit >= (people[-1] + people[0]):
            del people[0]
        del people[-1]
        answer += 1

    if len(people) == 1:
        answer += 1
    return answer


print(solution([70,50,80,50], 100))