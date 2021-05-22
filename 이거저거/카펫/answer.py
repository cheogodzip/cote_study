def solution(brown, yellow):
    hap = (brown + 4)/2
    print("hap : ", hap)
    gop = yellow + 2 * (hap) - 4
    print("gop : ", gop)
    zegop_hap = hap*hap - 2*gop
    cha = (zegop_hap - 2*gop)**(0.5)
    x = int((hap + cha)/2)
    y = int(hap - x)
    answer = [x,y]

    return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))