# 동적계획법 Dynamic Programming

* 이름과 상관이 없는 알고리즘
* 문제를 쪼개서 작은 문제의 답을 구하고 그것으로 더 큰 답을 구하는 것
* 분할정복과 비슷
* DP 구현 2가지
  * Top-Down
    * 재귀
    * 메모이제이션 Memoization
  * Botoom-Up
    * 반복문
    * 타뷸레이션 Tabulation
* DP Table에 작은 문제의 답을 기록하고 사용

* 메모이제이션
  * 중복 연산 방지를 위해 부분 문제의 답을 구해 Cache에 저장해두고 다음에 또 쓴다
  * 그때 그떄 필요한 부분만 구한다 Lazy-Evaluation
* 타뷸레이션
  * 부분 문제에 대한 답을 미리 다 구해 준다
  * 필요 없는 부분까지 모두 구한다 Eagle-Evaluation
  * 테이블을 채워 나간다는 의미