def solution(n):
    answer = [n]
    t = n
    while t != 1:
        if t%2 == 0:
            t = t / 2
            answer.append(t)
        elif t%2 == 1:
            t = 3*t+1
            answer.append(t)
        
            
    return answer