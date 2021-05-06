def solution(lottos, win_nums):
    answer = []
    temp = 0
    win = 0
    for i in lottos:
        if i == 0:
            temp += 1
        elif i in win_nums:
            win += 1
    # 최고 순위
    if (win + temp) <= 1:
        answer.append(6)
    else:
        answer.append(7 - (win + temp))
    # 최저 순위
    if win <= 1:
        answer.append(6)
    else:
        answer.append(7-win)
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))