def solution(a, b):
    x = int(str(a) + str(b))
    k = 2*a*b
    
    if x > k:
        answer = x
    elif x==k:
        answer = x
    else:
        answer = k

    return answer