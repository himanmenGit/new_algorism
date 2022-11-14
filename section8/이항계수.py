# 백준 문제 11051 숫자 카드
# https://www.acmicpc.net/problem/11051

"""
이항계수
nCr
r == 0 -> 1
n == r -> 1
n-1,r-1 + n-1,r
"""

"""
메모이제이션
"""
import sys

sys.setrecursionlimit(10 ** 7)

MOD = 10007

N, K = map(int, input().split())
cache = [[0] * 1001 for _ in range(1001)]


def bino(n, k):
    if cache[n][k]:
        return cache[n][k]

    if k == 0 or k == n:
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n - 1, k - 1) + bino(n - 1, k)
        cache[n][k] %= MOD

    return cache[n][k]


print(bino(N, K))

"""
타뷸레이션
"""

MOD = 10007

N, K = map(int, input().split())
cache = [[0] * 1001 for _ in range(1001)]

cache[0][0] = 1
for n in range(1, 1001):
    cache[n][0] = 1
    cache[n][n] = 1
    for k in range(1, n):
        if cache[n][k] == 0:
            cache[n][k] = (cache[n - 1][k - 1] + cache[n - 1][k]) % MOD

print(cache[N][K])
