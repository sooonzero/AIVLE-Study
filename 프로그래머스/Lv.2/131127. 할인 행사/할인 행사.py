from collections import Counter

def solution(want, number, discount):
    answer = 0
    wishlist = {}
    for w, n in zip(want, number):
        wishlist[w] = n
        
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c == wishlist:
            answer += 1
    
    
    return answer