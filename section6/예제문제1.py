# 예제문제 1
# 길찾기 문제
"""
보통 4방향이 많다 (6방향, 8방향 등도 있다)
방향값을 미리 코드에 짜두로 for문으로 순회하는 기법을 꼭 익혀 두자
"""

# dfs
# 우->하->좌->상
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
chk = [[False] * 100 for _ in range(100)]
N = int(input())


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


def dfs(y, x):
    chk[y][x] = True
    for k in range(4):
        ny = y + dy[k]
        nx = x + dy[k]
        if is_valid_coord(ny, nx) and not chk[ny][nx]:
            dfs(ny, nx)


# bfs
from collections import deque

# 우->하->좌->상
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
chk = [[False] * 100 for _ in range(100)]
N = int(input())


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    while len(q) > 0:
        y, x = q.popleft()
        chk[y][x] = True
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                q.append((ny, nx))
