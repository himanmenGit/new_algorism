# 음료수 얼려 먹기: 문제 설명
"""
연결 요소 찾기

NxM크기의 얼음틀이 있고 구멍이 있으면 0, 칸막이는 1
구멍이 뚫려 있는 부분끼리 상하좌우로 붙어 있는 경우 서로 연결되어 있다.
생성되는 총 아이스크림의 개수를 구하라
0 이 붙어 있으면 하나의 덩어리로 센다
"""

# 음료수 얼려 먹기: 문제 조건
"""
풀이시간 30분, 시간제한 1초 메모리 제한 128M

첫번째 줄에 얼음틀의 세로 길이 N과 가로길이 M (1 <=N <= 1_000)
두 번째 줄 부터 N+1줄 까지 얼음 틀의 형태가 주어짐
구멍은0, 칸만이는 1

한번에 만들수 있는 아이스크림의 개수를 출력
"""

"""
내 풀이
"""

from collections import deque

# N, M = map(int, input().split())
# board = []
# for n in range(N):
#     board.append(input())
N, M = 4, 5
board = [
    "00110",
    "00011",
    "11111",
    "00000",
]

# 우 좌 상 하
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

count = 0
visited = [[False] * M for _ in range(N)]
dq = deque()

for n in range(N):
    for m in range(M):
        pick = board[n][m]
        if pick == '0' and not visited[n][m]:
            # bfs
            dq.append((n, m))
            visited[n][m] = True
            while dq:
                y, x = dq.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny >= 0 and ny < N and nx >= 0 and nx < M:
                        if board[ny][nx] == '0' and not visited[ny][nx]:
                            dq.append((ny, nx))
                            visited[ny][nx] = True
            count += 1

print(count)

""" 
해답
DFS
"""

N, M = 4, 5
input_data = [
    "00110",
    "00011",
    "11111",
    "00000",
]
board = []
for i in range(N):
    board.append(list(map(int, input_data[i])))

for b in board:
    print(b)


def dfs(x, y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return
    if board[y][x] == 0:
        board[y][x] = 1

        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    return False


result = 0
for n in range(N):
    for m in range(M):
        if dfs(m, n) is True:
            result += 1

print(result)

# 미로탈출 : 문제 설명
"""
NxM크기의 미로가 존재
1,1이 시작위치 출구는 NxM
한번에 한칸씩 이동 가능 
괴물은 0, 괴물이 아니면 1
반드시 탍출 가능
탈출하기 위해 움직여야 하는 최소 칸 수 
시작칸 + 움직인칸 + 마지막칸
"""

# 미로 탈출: 문제 조건
"""
풀이시간 30분, 시간제한 1초, 메모리 제한 128
* 첫째 줄에 정수 N, M (4 <= N, M <= 200) 
* 둘째 줄에는 각각 0, 1 미로 정보가 주어지며 공백잆이 제시됨
* 시작,마지막캄은 항상 1
* 이동 칸 수?
"""

# N, M = map(int, input().split())
board = []
# for _ in range(N):
#     board.append(input())

N, M = 5, 6
input_data = [
    "101010",
    "111111",
    "000001",
    "111111",
    "111111"
]

for i in range(N):
    board.append(list(map(int, input_data[i])))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 1


def find(x, y):
    global result
    if x == M - 1 and y == N - 1:
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny <= -1 or ny >= N or nx <= -1 or nx >= M:
            continue

        result += 1
        find(nx, ny)
        break


find(0, 0)

print(result)

"""
해답
"""

# a = [
#     "1  0  5  0  7  0",
#     "2  3  4  5  6  7",
#     "0  0  0  0  0  8",
#     "14 13 12 11 10 9",
#     "15 14 13 12 11 10"
# ]


# N, M = map(int, input().split())
board = []
# for _ in range(N):
#     board.append(input())

N, M = 5, 6
input_data = [
    "101010",
    "111111",
    "000001",
    "111111",
    "111111"
]

for i in range(N):
    board.append(list(map(int, input_data[i])))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny <= -1 or ny >= N or nx <= -1 or nx >= M:
                continue

            if board[ny][nx] == 1:
                board[ny][nx] = board[y][x] + 1
                dq.append((nx, ny))

    return board[N - 1][M - 1]


print(bfs(0, 0))

for b in board:
    print(b)
