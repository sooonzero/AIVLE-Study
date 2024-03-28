def solution(k, m, score):
    answer = 0
    box = []
    score.sort(reverse=True)
    a = len(score)%m
    if  a> 0:
        score = score[:-a]
    
    for i in range(0,len(score),m):
            box = score[i:m+i]
            answer += (m * min(box)) 

    
    return answer