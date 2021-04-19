# 올바른 괄호 문자열
# 1. 감싸고 있는 문자가 없는 경우 -> () {} []
# 2. 올바른 괄호 문자열이 연속된 경우 -> ()() {}() []{}
# 3. 올바른 괄호 문자열을 감싸는 경우 -> ({})

s = "}]()[{"

def solution(s):
    answer = 0
    origin_s = list(s)
    for i in range(len(origin_s)):
        s = origin_s[i:] + origin_s[:i]
        stack = []
        while len(s) > 0:
            if s[0] in "({[":
                stack.append(s.pop(0))
            elif len(stack) == 0:
                break
            elif ((s[0] == ')') and (stack[-1] == '(')) or ((s[0] == '}') and (stack[-1] == '{')) or ((s[0] == ']') and (stack[-1] == '[')):
                    stack.pop()
                    s.pop(0)
            else:
                break
        if (len(s) + len(stack)) == 0:
            answer += 1
    return answer

print(solution(s))
