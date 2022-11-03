# 백준 문제 11724 연결요소의 개수
# https://www.acmicpc.net/problem/11724

"""
무방향 그래프
연결 요소의 개수
 - 끊어져 있는 그래프의 작은 모양의 수

정점수 N
간선수 M
N은 1보다 크고 1000보다 작다
M은 0보다 크고 Nx(N-1)/2 보다 작다
간선의 양끝점 u, v
1보다 크고 N보다 작으며 u,v가 같지 않은 정보는 1회 제공
"""

"""
내가 푼 문제 실패 이후 수정 (bfs로 품)
무방향 생각 못함
체크 포인트의 중복
"""
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
V = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    V[u][v] = 1
    V[v][u] = 1

from collections import deque

check = [False] * (N+1)
check[0] = True

dq = deque()


def bfs(n):
    dq.append(n)
    while dq:
        now = dq.popleft()
        if not check[now]:
            check[now] = True
            for i in range(1, N + 1):
                if V[now][i]:
                    dq.append(i)


count = 0
for n in range(N+1):
    if not check[n]:
        count += 1
        bfs(n)

print(count)

"""
bfs를 이용한 재귀 함수
"""

# 재귀 함수 제한 풀기
# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# V = [[0] * N for _ in range(N)]
# for _ in range(M):
#     a, b = map(lambda x: x - 1, map(int, input().split()))
#     V[a][b] = V[b][a] = 1
#
# ans = 0
# check = [False] * N
#
#
# def dfs(now):
#     for nxt in range(N):
#         if V[now][nxt] and not check[nxt]:
#             check[nxt] = True
#             dfs(nxt)
#
#
# for i in range(N):
#     if not check[i]:
#         ans += 1
#         check[i] = True
#         dfs(i)
#
# print(ans)
