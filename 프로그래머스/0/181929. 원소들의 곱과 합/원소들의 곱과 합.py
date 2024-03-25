def solution(num_list):
    answer = 0
    sum = 0
    gop = 1
    
    for x in num_list:
        sum += x
        gop *= x
    
    sum *= sum
    
    if sum > gop:
        answer = 1
        
    return answer