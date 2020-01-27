# Fibonacci Series using Dynamic Programming  
def fibonacci(n):  
    if n == 0:
        return 0
    elif n <= 2:
        return 1

    seq = [0] * n
    seq[0] = seq[1] = 1

    for i in range(2,n):
        seq[i]= seq[i-1]+seq[i-2]
    
    return seq[n-1]

print(fibonacci(10))