def solution(base,exp):
    if exp == 1:
        return base
    
    return base * solution(base,exp-1)

print("Result:",solution(2,2))