# 백준 문제 1302
# https://www.acmicpc.net/problem/1302

# 내가 푼 답
# dictionary와 sort를 이용
import sys
n = int(sys.stdin.readline())

dic = {}
for _ in range(n):
    title = sys.stdin.readline().replace("\n", "")
    if dic.get(title):
        dic[title] = dic[title] + 1
    else:
        dic[title] = 1

sorted_dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
max_value = sorted_dic[0][1]

title_list = []
for key, value in dic.items():
    if value == max_value:
        title_list.append(key)

title_list.sort()
print(title_list[0])

# resolve
# 해결 에서는 dic를 정렬 하는게 아니라 value만 뽑아와서 최대값을 확인함
sorted_dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
max_value = sorted_dic[0][1]

# >>>

max_value = max(dic.values())