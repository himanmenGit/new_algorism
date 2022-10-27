# 순열 permutations
# 모든 조합 가능한 경우의 수를 순서대로 살펴 볼 떄 용이

from itertools import permutations

v = [0, 1, 2, 3]

for i in permutations(v, 4):
    print(i)
print("-" * 100)

items = [62, 3, 40, 17, 5, 8, 26, 99]
max = (0, 0, 0)
for i in permutations(items, 2):
    if max[0] < sum(i):
        max = sum(i), i[0], i[1]
print(max[1], max[2])
print("-" * 100)

# 조합 combination
# 모든 조합 가능한 경우의 수를 순서와 상관없이 볼 떄 사용

from itertools import combinations

v = [0, 1, 2, 3]

for i in combinations(v, 4):
    print(i)

print("-" * 100)
items = [62, 3, 40, 17, 5, 8, 26, 99]
max = (0, 0, 0)
for i in combinations(items, 2):
    if max[0] < sum(i):
        max = sum(i), i[0], i[1]

print(max[1], max[2])
