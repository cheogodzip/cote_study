https://programmers.co.kr/learn/courses/30/lessons/43165

프로그래머스 타켓 넘버

주어진 숫자 배열의 원소를 더하거나 빼서 타켓 숫자를 만든다.

풀이방법
* 주어진 배열의 원소들을 모두 사용해서 타겟 숫자를 만들어야 한다.
* 각 원소마다 더하는 경우의 수, 빼는 경우의 수를 모두 계산한다.
* 0을 타겟 숫자로 만드는 것과 타겟 숫자에서 0을 만드는 경우의 수는 같다.
* 작성한 dfs 함수는 타겟 숫자에 원소마다 더하거나 빼서 마지막에 0이 되면 타겟 넘버를 만드는 경우의 수에 추가했다.