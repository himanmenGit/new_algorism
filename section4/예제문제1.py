# 완전 탐색 - 브루트 포스
# N개의 수를 입력 받아서 두 수를 뽑아 합이 가장 클 때는?
# 시간제한: 1초, 입력 2이상 1,000,000 이하
# 완전 탐색의 시간복잡도는 O(N^2)이므로 1초 안에 1,000,000개의 경우의 수를 계산 할 수 없다.

items = [62, 3, 40, 17, 5, 8, 26, 99]

# 1. 완전 탐색
max = (0, 0, 0)
for index, v in enumerate(items):
    for j in items[index + 1:]:
        sum = v + j
        if max[0] < sum:
            max = (sum, v, j)
print(max[1], max[2])

# 2. 정렬
# 보통의 정렬의 시간복잡도는 O(NlogN)
items.sort(reverse=True)
print(items[0], items[1])


