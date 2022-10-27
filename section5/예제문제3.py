# 백준 문제 1449
# https://www.acmicpc.net/problem/1449

# 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다
# 길이가 L 인 테이프를 무한개 가지고 있다.
# 물을 막을 때 적어도 그 위치의 좌우 0.5만큼 간격을 줘야 물이 안샌다
# 물이 새는 곳 위치와 데이프 길이 L이 있을 때 필요한 테이프의 최소 개수를 구하라
# 테이프를 겹쳐서 붙이는것도 가능하다
# N, L < 1000 자연수
# 위치 < 1000 자연수
# 못품 테이프를 덮듯이 미리 데이터를 채워서 하는걸 생각하지 못하고
# 값을 계산하려고만 함
# N, L이 값이 작기 때문에 이렇게 사용 할 수 있다.

N, L = map(int, input().split(" "))
P = list(map(int, input().split(" ")))
tile = [False] * 1001

for i in P:
    tile[i] = True

result = 0
x = 0
while x < 1001:
    if tile[x]:
        result += 1
        x += L
    else:
        x += 1
print(result)

# 좌표 압축
N, L = map(int, input().split(" "))
P = list(map(int, input().split(" ")))
P.sort()
result = 0
x = 0
v = P[0]
end = True
while len(P) > x:
    if P[x] > v or x == 0:
        result += 1
        v = P[x] + L-1
    x += 1

print(result)
