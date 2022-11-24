# DFS & BFS
"""
대표적인 그래프 탐색 알고리즘

탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
코딩 테스트에서 매우 자주 등장하는 유형!
"""

# 스택 자료구조
"""
먼저 들어온 데이터가 나중에 나가는 형식(선입후출)
입구와 출구가 동일한 형태로 스택을 시각화 할 수 있다.
"""

# python stack
stack = []

stack.append(5)
stack.append(4)
stack.append(3)
stack.pop()
stack.append(2)
stack.append(1)
stack.pop()

print(stack[::-1])
print(stack)

# 큐 자료주고
"""
먼저 들어온 데이터가 먼저 나가는 형식(선입선출)
입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 가능
파이썬에서는 deque(덱) 사용, popleft를 사용하여 제일 왼쪽 을 가져옴
"""
from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.popleft()
queue.append(2)
queue.append(1)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 재귀 함수
"""
자기 자신을 다시 호출하는 함수 DFS를 구현할 떄 자주 사용
재귀함수의 종료조건을 반드시 명시
종료 조건을 제대로 명시 하지 않으면 함수가 무한히 호출 될 수 있다.
import sys
sys.setrecursionlimit(10 ** 7) 로 최대 재귀 호출 횟수 수정 가능
"""


def recursive_function(i):
    if i == 3:
        return
    print("재귀 함수 호출")
    recursive_function(i + 1)


recursive_function(1)


# 재귀함수: 팩토리얼 계산

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))

# 재귀함수: 최대 공약수 계산(유클리드 호제법)
"""
두 개의 자연수에 대한 공통된 약수중 가장 큰값을 구하는의 대표적인 알고리즘이 유클리드 호제법
두 자연수 A,B에 대하여 (A>B) A를 B로 나눈 나머지를 R
이때 A와 B의 최대 공약수는 B와 R의 최대 공약수와 같다
"""


def GCD(a, b):
    if a % b == 0:
        return b

    return GCD(b, a % b)


print(GCD(192, 162))
