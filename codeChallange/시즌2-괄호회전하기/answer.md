https://programmers.co.kr/learn/courses/30/lessons/76502

프로그래머스 월간 코드 챌린지 시즌2 - 괄호 회전하기

글자를 하나씩 왼쪽으로 회전시키면서 주어진 괄호 문자열인지 올바른 문자인지 판단한다.

* 스택을 사용한다.
* 문자열을 한 문자씩 순회하면서 여는 괄호는 스택에 넣고 닫는 괄호라면 스택의 최상단 문자와 비교한다
    * 쌍이 이뤄진다면 스택과 문자열에서 해당 괄호를 제거한다.
    * 다르다면, 틀린 문자열로 처리한다.
  