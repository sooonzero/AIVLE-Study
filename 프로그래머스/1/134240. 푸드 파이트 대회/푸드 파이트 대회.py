def solution(food):
    a = []
    f = 0
    for x in food:
        for i in range (x//2):
            a.append(f)
        f += 1
    b = a.copy()
    a.append(0)
    b.reverse()
    
    answer = a+b
    
    return "".join(map(str,answer))