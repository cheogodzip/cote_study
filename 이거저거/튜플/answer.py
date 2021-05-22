def solution(s):
    answer = []
    temp = []
    s = s[2:-2]

    while True:
        pos = s.find("},{")
        if pos == (-1):
            temp.append(s.split(','))
            break
        temp.append(s[:pos].split(','))
        s = s[pos+3:]

    temp.sort(key=lambda x:len(x))
    for i in temp:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
                break

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))