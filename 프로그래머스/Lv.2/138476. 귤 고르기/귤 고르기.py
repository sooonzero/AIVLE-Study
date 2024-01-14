from collections import Counter

def solution(k, tangerine):
    answer = 0
    # Counter로 자료 변화 후 most_common으로 빈도수로 내림차순
    count = Counter(tangerine).most_common()
    # 최소 종류 계산
    for key, value in count:
        if k<= 0: break
        k -= value
        answer += 1
    return answer
