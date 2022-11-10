# 백준 문제 10815 숫자 카드
# https://www.acmicpc.net/problem/10815

"""
2초/256MB
상근이는 숫자카드 N개를 가지고 있다
정수 M개가 주어졌을 때 이 숫자카드를 상근이가 가지고 있는지 아닌지 구하는 것

첫줄
숫자카드 개수 N(1<=N<=500,000)
둘째 줄
숫자 카드에 적혀있는 정수 List(M) (-10,000,000 <= List(N) <= 10,000,000)
모든 카드는 유일한 수
셋째 줄
M (1 <= M <= 500,000)
넷쨰 줄
가지고 있는 숫자카드 인지 아닌지 구해야할 M개의 정수공백구분 (-10,000,000 <= List(M) <= 10,000,000)


-> 기존에는 입력 받은 데이터를 list로 바꿔서 in으로 체크함 (타임아웃)
-> N_list를 set으로 바꾸고 동일하게 in으로 체크함 (성공)
-> set이 list보다 탐색이 빠르다
"""

# import sys
# import math
#
# input = sys.stdin.readline
#
# N = int(input())
# N_list = list(map(int, input().split(" ")))
# M = int(input())
# M_list = list(map(int, input().split(" ")))
#
# N_list.sort()
# result = [0] * M
#
# for index, m in enumerate(M_list):
#     top = len(N_list)
#     bottom = 0
#     mid = (bottom + top) // 2
#     for i in range(int(math.log(len(N_list), 2))):
#         if m >= N_list[mid]:
#             bottom = mid
#         else:
#             top = mid
#         mid = ((bottom + top) // 2)
#     if m in N_list[bottom: top]:
#         result[index] = 1
#
# print(" ".join(map(str, result)))

# N = int(input())
# N_list = set(input().split())
# M = int(input())
# M_list = input().split()

# for index, m in enumerate(M_list):
#     if m in N_list:
#         result[index] = 1

# print(" ".join(map(str, result)))


"""
bisect를 이용한 구현
"""

from bisect import bisect_left, bisect_right

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

result = []

# bisect_left만 사용
for index, m in enumerate(M_list):
    l = bisect_left(N_list, m)
    try:
        if N_list[l] == m:
            result.append(1)
        else:
            result.append(0)
    except Exception:
        result.append(0)

# bisect_left는 요소를 찾은 index를 반환 (찾은 요소의 왼쪽에 삽입하기 위함)
# bisect_right는 요소를 찾은 index+1을 반환 (찾은 요소의 오른쪽에 삽입하기 위함)
# bisect_right - bisect_left가 0 보다 크면 찾은 것
# bisect_right - bisect_left가 0이면 못 찾은것
for index, m in enumerate(M_list):
    l = bisect_left(N_list, m)
    r = bisect_right(N_list, m)
    if r - l > 0:
        result.append(1)
    else:
        result.append(0)

print(*result)