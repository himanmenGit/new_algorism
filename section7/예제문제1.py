# 백준 문제 2512 예산
# https://www.acmicpc.net/problem/2512

"""
low, mid, high라는 구간을 잡아서
해당 구간의 위치만 바꾸어 주도록 생각하지 못함.

리스트의 위치로만 계산하려다 실패
"""
import sys

input = sys.stdin.readline

m = int(input())
n = list(map(int, input().split()))
r = int(input())

n.sort()

if sum(n) <= r:
    print(n[-1])
elif n[0] >= r:
    print(int(sum(n) // m))
else:
    low = 0
    high = max(n)
    mid = (low + high) // 2
    ans = 0

    def is_possible(mid):
        return r >= sum([(min(v, mid)) for v in n])

    while low <= high:
        if is_possible(mid):
            low = mid + 1
            ans = mid
        else:
            high = mid - 1

        mid = (low + high) // 2

    print(ans)