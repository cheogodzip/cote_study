def search(current, target, words, path, visited):
    # 한글자만 다른 것 찾기
    print("current", current)
    print("path", path)
    temp = []
    for word in words:
        # 이미 지나온 것, 지나친 것은 다시 가지 않는다.
        if (word in path) or (word in visited):
            continue
        diff = 0
        for ch in range(len(word)):
            if current[ch] != word[ch]:
                diff += 1
                if diff >= 2:
                    break
        if diff == 2:
            continue
        temp.append(word)
    visited += temp
    print("temp", temp)
    print("visited", visited)
    if (target in temp):
        current = target
        path.append(current)
        return len(path)

    if len(temp) == 0:
        return 0

    elif len(temp) == 1:
        current = temp[0]
        path.append(current)
        return search(current, target, words, path, visited)

    score = 0
    for p in temp:
        t = search(p, target, words, path + [p], visited)
        if t > 0:
            if (score == 0) or (t < score):
                score = t
    return score

def solution(begin, target, words):
    answer = search(begin, target, words, [], [])
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 3