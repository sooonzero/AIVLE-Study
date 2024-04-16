def solution(arr):
    answer = []
    
    while True:
        for x in arr:
            for i in range(x):
                answer.append(x)
        break
    return answer