# 전체에서 체육복 못 빌리는 학생 수 만큼 빼기
def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    reserve_and_lost = lost_set & reserve_set

    lost_set -= reserve_and_lost
    reserve_set -= reserve_and_lost
    
    
    
    answer = n
    for x in lost_set:
        if x-1 in reserve_set:
            reserve_set.remove(x-1)
            answer += 1
        elif x+1 in reserve_set:
            reserve_set.remove(x+1)
            answer += 1
            
    answer -= len(lost)
    
    
    return answer

def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    reserve_and_lost = lost_set & reserve_set

    lost_set -= reserve_and_lost
    reserve_set -= reserve_and_lost

    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set -= {i - 1, }
        elif i + 1 in lost_set:
            lost_set -= {i + 1, }

    return n - len(lost_set) 