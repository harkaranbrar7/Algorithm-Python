def solution(n):
    if n == 1:
        return n
    
    return n * solution(n-1)



print("Result:", solution(5))