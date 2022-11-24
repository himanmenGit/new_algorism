# DFS (Depth-First-Search)
"""
깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색
DFS는 스택 혹은 재귀를 이용함
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최산단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면
    그 노드를 스택에 넣고 방문 처리
    방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냄
3. 더 이상 2번의 과정을 수행할 수 없을 떄까지 반복

"""


def dfs(graph, v, visited):
    # 방문처리
    visited[v] = True
    print(v, end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
dfs(graph, 1, visited)
