# 백준 문제 11047
# https://www.acmicpc.net/problem/11047

coin_count, max_amount = [int(x) for x in input().split(" ")]
coins = [int(input()) for _ in range(coin_count)]
coins.sort(reverse=True)
# coins.reverse() 도 가능
count = 0
for c in coins:
    _count, _remain = divmod(max_amount, c)
    count += _count
    max_amount = _remain

print(count)

