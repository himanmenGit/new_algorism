# 구현 (Implementation)
"""
구현이란 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
- 풀이를 떠올리는 것은 쉽지만 소스코드를 옮기기 어려운 문제

* 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
* 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는문제
* 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
* 적절한 라이브러리를 찾아서 사용해야 하는 문제

일반적으로 문제에서의 2차원 공간은 행렬의 의미로 사용
"""

# 상하좌우: 문제 설명
"""
여행가 A 는 NxN 크기의 정사각형 공간위에 있다.
이 공간은 1x1크기의 정사각형
가장 왼쪽 위 좌표는 (1,1), 가장 오른쪽 아래 좌표는 (N,N)
상,하,좌,우 방향으로 이동 가능
시작 좌표는 항상 (1,1)

계획서를 확인하여 여행가를 이동시키는 것
계획서는 L,R,U,D 중 하나의 문자가 반복적으로 적혀 있다
L: 왼쪽 한칸
R: 오른쪽 한칸
U: 위로 한칸
D: 아래로 한칸

여행가 A가 NxN크기의 공간을 벗어나는 움직임은 무시 된다.
(1,1)의 위치에서 L,U등을 만나면 무시 된다.
"""

# 상하좌우: 문제 조건
"""
풀이시간: 15분, 시간제한 2초, 메모리제한: 128M
입력
첫째 줄에 공간의 크기를 나타내는 N 1<=N<=100
둘째 줄에 여행가 A가 이동할 계획서 내용 1<=이동횟수<=100

출력
A가 최종적으로 도착할 지점의 좌표(X,Y)를 공백기준으로 출력
"""

"""
내 풀이
배열을 만들어 그렸다
"""
N = 5
A = ["R", "R", "R", "U", "D", "D"]

atoi = {"R": 0, "U": 1, "L": 2, "D": 3}

# (y, x)
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

y, x = 0, 0
board = [[0] * N for _ in range(N)]
board[0][0] = 1
for a in A:
    ny = y + dy[atoi[a]]
    nx = x + dx[atoi[a]]
    if ny >= N or ny < 0 or nx >= N or nx < 0:
        continue
    y = ny
    x = nx
    board[y][x] = 1

print(y + 1, x + 1)

"""
해답 풀이
값 만으로 풀이
"""
N = 5
A = ["R", "R", "R", "U", "D", "D"]
y, x = 1, 1

# (y, x)
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for a in A:
    for i in range(len(move_types)):
        if move_types[i] == a:
            ny = y + dy[i]
            nx = x + dx[i]
    if ny < 1 or nx < 1 or ny > N or ny > N:
        continue
    y, x = ny, nx

print(y, x)

# 시각: 문제 설명
"""
정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초 까지 모든 시각중
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
1을 입력 했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각

세어야 하는 시각
00시 00분 03초
00시 13분 30초

세면 안되는 시각
00시 02분 55초
01시 27분 45초
"""

# 시각: 문제 조건
"""
풀이시간 15분, 시간제한 2초
첫째 줄에 정수 N 0 <= N <=23
00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각중 
3이 하나라도 포함되는 모든 경우의 수를 출력
"""

"""
내 풀이
지정된 시간부터 00:00:00 까지 하나씩 내려가면서 계산
"""

N = 5

loop_count = (N + 1) * 60 * 60
count = 0
start = {
    "H": N,
    "M": 59,
    "S": 59
}

for c in range(loop_count):
    word = "".join(list(map(str, start.values())))
    if "3" in word:
        count += 1

    if 0 < start["S"] < 60:
        start["S"] -= 1
    else:
        start["S"] = 59

        if 0 < start["M"] < 60:
            start["M"] -= 1
        else:
            start["M"] = 59

            if 0 < start["H"] < 24:
                start["H"] -= 1

    if start["H"] == -1 and start["M"] == 0 and start["S"] == 0:
        break

print(count)

"""
해답 풀이
각 시간을 3중 for문으로 돌며 계산
"""

N = 5
count = 0
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) + str(m) + str(s):
                count += 1

print(count)
