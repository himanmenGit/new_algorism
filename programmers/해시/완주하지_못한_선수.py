# 프로그래머스 - 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576


from collections import defaultdict


def solution(participant, completion):
    p_dict = defaultdict(int)
    for p in participant:
        p_dict[p] += 1

    c_dict = defaultdict(int)
    for c in completion:
        c_dict[c] += 1

    answer = ''
    for key, value in p_dict.items():
        if value != c_dict.get(key):
            answer = key

    return answer


# resolve

from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys)[0]
