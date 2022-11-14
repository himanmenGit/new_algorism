# 백준 문제 2748 숫자 카드
# https://www.acmicpc.net/problem/2748

"""
피보나치 수열
앞의 두 수를 더해 다음 수를 만드는 것
f(0) = 0
f(1) = 1
f(i+2) = f(1+2) + f(i)
"""

"""
첫번 쨰 풀이
"""
n = int(input()) + 1

ans = 0
if n <= 2:
    if n != 0:
        ans = 1
else:
    dp = [-1] * n
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n):
        dp[i] = dp[i - 2] + dp[i - 1]
    ans = dp[n - 1]
print(ans)

"""
두번 째 풀이
"""

n = int(input()) + 1

if n < 3:
    if n - 1 == 0:
        print(0)
    else:
        print(1)
else:
    dp = [-1] * n

    dp[0] = 0
    dp[1] = 1
    dp[2] = 1


    def f(n):
        if n < 3:
            return dp[n]

        if dp[n] > 0:
            return dp[n]
        result = f(n - 1) + f(n - 2)

        dp[n] = dp[n - 2] + dp[n - 1]
        return result


    f(n - 1)
    print(dp[n - 1])

"""
메모이제이션 좋은 풀이
"""

# 90이하니까
cache = [-1] * 91
cache[0] = 0
cache[1] = 1


def f(n):
    if cache[n] == -1:
        cache[n] = f(n - 1) + f(n - 2)
    return cache[n]


print(f(int(input())))

"""
타뷸레이션 좋은 풀이
"""

N = int(input())
cache = [-1] * 91
cache[0] = 0
cache[1] = 1

for i in range(2, N + 1):
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[N])
