# 백준 문제 2164
# https://www.acmicpc.net/problem/2164
# 시뮬레이션 문제
# N이 1 ~ 500,000 까지라 시간복자도를 생각해야 한다.

# 직접 푼 답 - 시간초과
# 시간복잡도를 생각하지 않음 O(N)
n = int(input())
a = list(range(n, 0, -1))

for i in range(len(a) - 1):
    a.pop()
    a.insert(0, a.pop())

print(a[0])

# solved
# queue를 이용해서 가능
from collections import deque

n = int(input())
q = deque(list(range(1, n + 1)))

for i in range(len(q) - 1):
    q.popleft()
    q.append(q.popleft())

print(q[0])
