# 백준 문제 9012
# https://www.acmicpc.net/problem/9012
# 전형적인 stack을 이용한 문제
# stack을 이용할 것이라고 예상했지만 풀이 과정은 생각해내지 못하였음
# 최초 count룰 이용하여 풀려 했으나 배운 자료구조를 토대로 하려다 보니 버벅거림
# count 변수를 이용하던 stack을 이용하던 순서와 개수가 맞아야 햐는 문제

## 1
t = int(input())
for _ in range(t):
    skt = []
    is_vps = True
    for ch in input():
        if ch == "(":
            skt.append(ch)
        if ch == ")":
            if len(skt) > 0:
                skt.pop()
            else:
                is_vps = False
                break

    if len(skt) > 0:
        is_vps = False

    print("YES" if is_vps else "NO")

## 2 - 틀림
## 예제 입력2를 보지 않고 작성하여 실패!
## ())(()
t = int(input())
for _ in range(t):
    ch = input()
    if ch.startswith(")") or ch.count("(") != ch.count(")"):
        is_vps = False
    else:
        is_vps = True
    print("YES" if is_vps else "NO")