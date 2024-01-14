# dictionary로 메모리를 사용

from collections import Counter

def solution(topping):
    answer = 0
    cs = Counter(topping)
    br = set()
    
    for t in topping:
        cs[t] -= 1
        br.add(t)
        
        if cs[t]==0:
            cs.pop(t)
            
        if len(cs) == len(br):
            answer += 1
            
    return answer
