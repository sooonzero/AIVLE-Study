def solution(ineq, eq, n, m):
    if ineq == '>':
        if eq == '=':
            answer = bool(n >= m)
        else:
            answer = bool(n > m)
    else:
        if eq == '=':
            answer = bool(n <= m)
        else:
            answer = bool(n < m)
            
    if answer == True:
        answer = 1
    else:
        answer = 0
    return answer