def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        temp = ""
        for sk in tree:
            if sk in skill:
                temp += sk
        if (temp == "") or (temp == skill[:len(temp)]):
            answer += 1
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))