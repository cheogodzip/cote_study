# 유클리드 호제법
# A > B 일 때, A mod B 를 R 이라고 하면
# A 와 B의 최대공약수는, B와 R의 최대 공약수와 같다

def euclidean(a,b):
    if b == 0:
        return a
    return euclidean(b, a%b)

print(euclidean(192, 190))