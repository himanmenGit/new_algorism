# 백준 문제 2178 미로 탐색
# https://www.acmicpc.net/problem/2178

"""
1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

1은 이동할 수 있는 칸
0은 이동 할 수 없는 칸
(1,1) 출발하여 (N, M)위치까지 최소의 칸수 구하기
인전합 칸으로만 이동 가능
첫줄 두 정수 N, M (N은 2보다 크거나 같고 M은 100보다 작거나 같다)
"""
from collections import deque

N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 좌 하 우 상
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def is_valid_coord(y, x):
    return 0 <= x < M and 0 <= y < N


# N, M까지 가야함
def bfs():
    check = [[False] * M for _ in range(N)]
    check[0][0] = True
    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        y, x, d = dq.popleft()
        if x == M - 1 and y == N - 1:
            return d

        nd = d + 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not check[ny][nx]:
                check[ny][nx] = True
                dq.append((ny, nx, nd))


print(bfs())

# from collections import deque
#
# N, M = map(int, input().split())
# board = [input() for _ in range(N)]
#
# dy = [0, 1, 0, -1]
# dx = [-1, 0, 1, 0]
#
#
# def is_valid_coord(y, x):
#     return 0 <= y < N and 0 <= x < M
#
#
# def bfs():
#     chk = [[False] * M for _ in range(N)]
#     chk[0][0] = True
#     dq = deque()
#     dq.append((0, 0, 1))
#     while dq:
#         y, x, d = dq.popleft()
#
#         if y == N -1 and x == M - 1:
#             return d
#
#         nd = d + 1
#         for k in range(4):
#             ny = y + dy[k]
#             nx = x + dx[k]
#             if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
#                 chk[ny][nx] = True
#                 dq.append((ny, nx, nd))
#
# print(bfs())
