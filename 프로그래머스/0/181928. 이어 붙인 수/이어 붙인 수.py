def solution(num_list):
    answer = 0
    holl = []
    jjak = []
    
    for x in num_list:
        if x%2 == 0:
            jjak.append(x)
        else:
            holl.append(x)
    
    for i in range(len(holl)):
        answer += (10**(len(holl)-i))/10 * holl[i]
        
    for i in range(len(jjak)):
        answer += (10**(len(jjak)-i))/10 * jjak[i]
        
    
    return answer