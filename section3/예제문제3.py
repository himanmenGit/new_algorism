# 백준 문제 11286
# https://www.acmicpc.net/problem/11286

# heapq에 절대값으로 입력한 데이터를 넣는다
# 입력한 데이터를 배열에 저장한다
# heapq에서 최소값을 빼서 음수로 변환 후 배열에서 확인한다. 없으면 양수로 한번더 확인
# 배열의 값을 출력 후 삭제 한다
# 시간초과 ㅠㅠ
# 이후 heap에 튜플을 넣을 수 있는 것을 깨닫고 수정
# 튜플을 넣으면 어떤값으로 min-heap이 동작하는지?
import heapq as hq
import sys

pq = []
n = int(input())
for _ in range(n):
    i = int(sys.stdin.readline())
    if i != 0:
        hq.heappush(pq, (abs(i), i))
    if i == 0:
        if len(pq) > 0:
            print(hq.heappop(pq)[1])
        else:
            print(0)

# resolve 2
# 우선순위 큐를 2개 사용하는 방법
# 음수/양수를 분리하여 비교

import heapq as hq
import sys

plus_heap = []
minus_heap = []
input = sys.stdin.readline
for _ in range(int(input())):
    x = int(input())

    if x > 0:
        hq.heappush(plus_heap, x)
    if x < 0:
        hq.heappush(minus_heap, abs(x))

    if x == 0:
        if len(plus_heap) > 0:
            if len(minus_heap) > 0:
                # 2개다 있는경우
                if minus_heap[0] > plus_heap[0]:
                    print(hq.heappop(plus_heap))
                else:
                    print(-hq.heappop(minus_heap))
            else:
                # plus_heap만 있는 경우
                print(hq.heappop(plus_heap))
        else:
            if len(minus_heap) > 0:
                # minus_heap만 있는 경우
                print(-hq.heappop(minus_heap))
            else:
                # 2개다 없는 경우
                print(0)
