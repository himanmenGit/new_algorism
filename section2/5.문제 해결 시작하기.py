# 코테에 필요한 기본 지식

# 입출력 함수
n = int(input())
print(n + 4)

## 문자열 분할
n = input().split()
print(n)

# map을 사용한 언패킹
# map(func, iterable)
a, b = map(int, input().split())
print(a, b)

# 빠른 입출력
# import sys 사용
# 백준 15552. 빠른 A+B
import sys

sys.stdin.readline()
for _ in range(100000):
    n = int(sys.stdin.readline())
    print(n)

# 오버 플로우
# 자료형이 담을 수 있는 범위 초과 한경우
# python은 고려하지 않아도 됨