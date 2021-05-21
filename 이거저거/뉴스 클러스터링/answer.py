def solution(str1, str2):
    str1_set = [str1[i:i + 2].upper() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    str2_set = [str2[i:i + 2].upper() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    intersection = []

    for i in str1_set:
        if i in str2_set:
            intersection.append(i)
            str2_set.remove(i)

    union = str2_set + str1_set

    if len(intersection) + len(union) == 0:
        return 65536

    return int((len(intersection) / len(union)) * 65536)


print(solution("FRANCE","french"))
print(solution("handshake","shake hands"))
print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))