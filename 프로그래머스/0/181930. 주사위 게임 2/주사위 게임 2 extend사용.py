def solution(a, b, c):
    answer = 0
    count = []
    count.extend([a,b,c])
    k = len(set(count))
    
    x = a+b+c
    y = a**2 + b**2 + c**2
    z = a**3 + b**3 + c**3
    
    if k == 3:
        answer = x
    elif k == 2:
        answer = x*y
    elif k == 1:
        answer = x*y*z
    
    return answer
