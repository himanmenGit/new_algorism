# IT 기업 코딩 테스트 최신 출제 경향
"""
가장 출제 빈도가 높은 알고리즘 유형
* 그리디 (쉬운 난이도)
* 구현
* DFS/BFS를 활용한 탐색
"""

# 알고리즘 성능 평가
"""
복잡도
* 시간 복잡도: 수행 시간 분석
* 공간 복잡도: 메모리 사용량 분석

빅오 표기법
* 가장 빠르게 증가하는 항만을 고려 함
* 3N^3 + 5N^2 + 1_000_000 -> O(N^3)

좋음
O(1)        상수 시간
O(logN)     로그 시간
O(N)        선형 시간
O(NlogN)    로그 선형 시간
O(N^2)      이차 시간
O(N^3)      삼차 시간
O(2^n)      지수 시간
나쁨
"""

# 시간 복잡도 계산해보기 1)
"""
시간복잡도 O(N)
총 데이터의 개수 만큼 summary에 값이 더해지므로 N만큼 선형적으로 수행시간이 증가 한다 
"""
array = [3, 5, 1, 2, 4]
summary = 0

for x in array:
    summary += x
print(summary)

# 시간 복잡도 계산해보기 2)
"""
시간복잡도 O(N^2)
총 데이터의 개수 * 개수 만큼 증가한다
모든 2중 반복문의 시간복잡도가 O(N^2)인것은 아니다.
반복문이 수행될 떄마다 별도의 함수가 수행된다면 해당 함수 내의 시간 복잡도 까지 고려 해야함
"""
array = [3, 4, 1, 2, 4]

for i in array:
    for j in array:
        temp = i * j
        print(temp)

# 알고리즘 설계 Tip
"""
연사 횟수가 5억을 넘어가는 경우 
* C언어 기준으로 1~3초 가량 소요됨
* Python기준으로 5~15초 가량 소요됨

O(N^3)dls 경우 125,000,000,000 (2500초)
코팅테스트 문제에서 시간은 통상 1~5초 가량에 유의

실제 테스트에서는 서버가 Python을 1초에 2천만번 정도 처리 할 수 있다고 가정하면서 풀기
"""

# 요구 사항에 따라 적절한 알고리즘 설계하기
"""
문제에서 가장 먼저 확인해야 하는것은 시간제한(수행시간 요구사항)
시간 제한이 1초인 경우
* N 범위가 500인 경우 O(N^3)는 풀 수 있다.
* N 범위가 2000인 경우 O(N^2)는 풀 수 있다.
* N 범위가 100,000인 경우 O(NlogN)는 풀 수 있다.
* N 범위가 10,000,000인 경우 O(N)는 풀 수 있다.
"""

# 일반적인 알고리즘 문제 해결 과정
"""
1. 지문 꼼꼼하게 읽고, 컴퓨터적인 사고로 문제를 단계적으로 쪼개어 문제를 정의
2. 요구사항(복잡도) 분석 - 성능에 대한 생각
3. 문제 해결을 위한 아이디어 찾기
4. 소스코드 설계 및 코딩

문제 출제자들은 핵심 아이디어를 캐치 한다면, 간결하게 소스코드를 작성 할수 있도록 문제를 출제 함.
"""

# 리스트 컴프리헨션
"""
2차원 리스트 초기화 시 주의사항
아래와 같이 작성할 경우 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식됨.
"""
# 잘못된 예
m, n = 10, 10
array = [[0] * m] * n

# 좋은 예
array = [[0] * m for _ in range(n)]

# 자주 사용되는 표준 입력/출력 방법
"""
- 입력
import sys
sys.stdin.readline() - 빠른 문자열 입력 함수
input - 한줄의 문자열을 입력 받는 함수
map - 리스트의 모든 원소에 각각 특정한 함수를 적용 할 때

- 출력
print()는 출력이후 줄바꿈이 되는데 원치 않을 경우 end 키워드를 사용한다. 
"""
list(map(int, input().split()))
a, b, c, = map(int, input().split())

# 람다 표현식
"""
lambda
매개변수와 결과값을 한줄에 사용
"""
print((lambda a, b: a + b)(3, 7))

"""
지정된 Key 값으로 정렬하도록 사용
"""
array = [("홍길동", 50), ("이순신", 32), ("아무개", 74)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

"""
여러개의 리스트에 적용
"""
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b: a + b, list1, list2)
print(list(result))

# 실전에서 유용한 표준 라이브러리
"""
* 내장 함수
* itertools - 반복 데이터 처리를 하기 위함, 순열, 조합 (모든 경우의 수), 완전 탐색 유형
* heapq - 힙 자료구조, 우선순위 큐 기능을 구현, 다익스트라(최단경로)
* bisect - 2진 탐색 기능 제공
* collections - 덱, 카운터 등의 유용한 자료구조
* math - 수학적 기능
"""

# 자주 사용되는 내장 함수
"""
sorted
sorted with key
"""
result = sorted([9, 1, 8, 5, 4])  # 오름차순
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)  # 내림차순

array = [("홍길동", 50), ("이순신", 32), ("아무개", 74)]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1], reverse=True))

"""
순열과 조합
모든 경우의 수를 고려 해야 할 때
순열: 서로 다른 n개에서 서로다른 r개를 선택하여 일렬로 나열 하는것
    {'A', 'B', 'C'} -> 'ABC', 'ACB', "BAC', 'BCA', 'CAB', 'CBA'
    조합 가능한 모든 순서를 고려하여 경우의 수를 선택
    nPr -> permutation
조합: 서로 다른 n개에서 순서에 상관없이 서로 가른 r개를 선택 하는것
    {'A', 'B', 'C'}에서 순서를 고려 하지 않고 두개를 뽑는 경우 'AB', 'AC', 'BC'
    지정된 개수로 가능한 순서와 강관없이 수를 선택
    nCr -> combination
"""

# 순열
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# 조합
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

# 중복 순열과 중복 조합

from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

# Counter
"""
collections 라이브러리에 포함 
등장 횟수를 세는 기능
반복 가능한(iterable) 객체를 주면 내부의 원소가 몇번씩 등장했는지 알려줌
"""

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(Counter('blue'))
print(Counter('green'))
print(dict(counter))

# 최대 공약수와 최소 공배수
import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


a = 21
b = 14

print(math.gcd(21, 14))  # 최대 공약수 (GCD)
print(lcm(21, 14))  # 최소 공배수 (LCM)
