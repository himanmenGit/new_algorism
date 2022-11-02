# DFS (Depth First Search) 깊이 우선 탐색

"""
* 탐색알고리즘 (완전 탐색)
* 깊이를 우선으로 탐색을 한다
* 스택 or 재귀를 이용해서 구현함
    * 일반적으로는 재귀를 많이 사용
    * 재귀를 사용한다는 것은 컴퓨터 구조적으로 스택을 사용하는것으로 비슷하다.
* root노드에서 탐색을 시작하고 root에서 끝난다.
* 다음 Node가 있는 Node까지 탐색 하고 다음 Node가 없으면 돌아와서 다른 Node를 탐색 한다.
"""

# 인접행렬 또는 인접리스트에 그래프 데이터를 추가한다
# 인접행렬
adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
adj[2][3] = adj[2][4] = 1
adj[5][6] = 1
adj[7][8] = adj[7][9] = 1
adj[9][10] = adj[9][11] = adj[9][12] = 1


# 재귀 함수로 구현
# 현재 방문한 Node번호
def dfs(now):
    for nxt in range(13):
        # 현재 방문한 Node에서 연결된 Node를 찾아 방문 한다.
        if adj[now][nxt]:
            print(now, nxt)
            dfs(nxt)


dfs(0)


# stack으로 구현한 dfs
def dfs_stack():
    # root에서 시작
    stx = [0]

    while stx:
        print(stx)
        # 방문한 Node 처리
        now = stx.pop(-1)
        # 오른쪽 부터 확인 왜(?)
        for nxt in range(12, 0, -1):
            if adj[now][nxt]:
                stx.append(nxt)


dfs_stack()
