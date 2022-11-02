# BFS (Breadth First Search) 너비 우선 탐색

"""
* 탐색알고리즘 (완전탐색)
* 너비를 우선으로 탐색 한다
* 큐를 사용해서 구현한다
* root에서 시작
    * 같은 높이의 Node를 모두 탐색하면서 진행한다
"""

adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
adj[2][3] = adj[2][4] = 1
adj[5][6] = 1
adj[7][8] = adj[7][9] = 1
adj[9][10] = adj[9][11] = adj[9][12] = 1

from collections import deque


# 큐를 이용한 너비 우선 탐색
def bfs():
    q = deque()
    q.append(0)

    while q:
        print(q)
        now = q.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                q.append(nxt)


bfs()
