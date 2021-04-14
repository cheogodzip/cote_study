def solution(loc):
    answer = []
    temp_int = 0
    for i in loc:
        if i in '0123456789':
            temp_int += int(i)
        else:
            answer.append(i)
    answer.sort()
    return ''.join(answer)+str(temp_int)
print(solution("K1KA5CB7"))
# 문자열 재정렬