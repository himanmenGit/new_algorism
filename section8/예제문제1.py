# 백준 문제 11726 타일링
# https://www.acmicpc.net/problem/11726

"""
2xN크기의 직사각형을 1x2, 2x1로 채우는 방법의 수를 구하기
1 <= N <= 1000
2xN크기 채우는 방법의 수를 10,007로 나눈 나머지를 출력
"""

"""
마지막을 채우는 직사각형은 1x2, 2x1밖에 없다.
f(1) = 1
f(2) = 2
f(3) = 3
f(n) = f(n-1) + f(n-2)
"""

"""
타뷸레이션
"""
MOD = 10007
n = int(input())

dp = [-1] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= MOD

print(dp[n])

"""
메모이제이션
"""
import sys

sys.setrecursionlimit(10 ** 9)

MOD = 10007
n = int(input())

dp = [-1] * 1001


def f(n):
    if n == 1:
        dp[1] = 1
    elif n == 2:
        dp[2] = 2
    else:
        if dp[n] < 0:
            dp[n] = f(n - 1) + f(n - 2)
            dp[n] %= MOD
    return dp[n]


print(f(n))
