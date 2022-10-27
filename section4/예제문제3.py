# 백준 문제 2309
# https://www.acmicpc.net/problem/2309

# 9명의 난쟁이 중 7명의 키의 합이 100이 되는 조건을 찾으면 됨

items = [20, 7, 23, 19, 10, 15, 25, 8, 13]

# 1. combination이용하여 풀이
from itertools import combinations

# items = [int(input()) for _ in range(9)]

result = None
for v in combinations(items, 7):
    if sum(v) == 100:
        result = list(v)

result.sort()
for i in result:
    print(i)
print("-" * 100)


# 2. 키의 합으로 계산

items = [int(input()) for _ in range(9)]

def run(items):
    total = sum(items)
    items.sort()
    for i in range(8):
        for j in range(i + 1, 9):
            if total - items[i] - items[j] == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(items[k])
                return


run(items)
