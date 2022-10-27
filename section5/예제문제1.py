# 탐욕법 - 그리디

# 동전 거스름돈 문제
# 10, 50, 100, 500원 동전들을 무한하게 갖고 있다.
# 손님에게 800원을 거슬러주려고 할 때 동전을 최소한으로 주는 방법은?
# 500-1, 100-3 총 4개가 최선
# 가장 단위가 큰 동전부터 주는 경우
# 그리디로 풀 수 있다.
# 큰 동전이 작은 동전의 항상 배수 이다.

coins = [10, 50, 100, 500]
coins.sort(reverse=True)

n = 800
count = 0
for c in coins:
    _count, _remain = divmod(n, c)
    count += _count
    n = _remain

print(count)

# 동전 거스름돈 문제
# 100, 400, 500원 동전을 무한하게 갖고 있다.
# 손님에게 800원을 거슬려 주려고 할 때 동전을 최소한으로 주는 방법은?
# 그리디로 풀수 없다.
# 400-2 총 2개가 최소
# 완전탐색? DP?

# 그리디 판단 로직

coins = [10, 50, 100, 500]
max_coin = max(coins)

b_greedy = True
for c in coins[:-1]:
    if max_coin % c > 0:
        b_greedy = False

# 그리디 문제의 어려운점은 해당 문제가 그리디 인지 아닌지 판단하는게 어렵다
