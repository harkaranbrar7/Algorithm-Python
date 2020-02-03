def solution(n):
    if n ==1:
        return n
    
    else:
        return n * solution(n-1)



print(solution(7))