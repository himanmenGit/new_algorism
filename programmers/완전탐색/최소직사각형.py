# 프로그래머스 - 최소 직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

z = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(max([max(x) for x in z]))
# print(max(z))
# w = []
# h = []
# for v in z:
#     if v[1] > v[0]:
#         w.append(v[1])
#         h.append(v[0])
#     else:
#         w.append(v[0])
#         h.append(v[1])
#
# print(max(w) * max(h))


def solution(sizes):
    w = list(map(lambda x: x[1] if x[1] > x[0] else x[0], sizes))
    h = list(map(lambda x: x[0] if x[1] > x[0] else x[1], sizes))
    return max(w) * max(h)
