# Fibonacci Series using Dynamic Programming  
def fibonacci(n): 
    # check for n is zero or less than two 
    
    if n == 0:
        return 0
    elif n <= 2:
        return 1

    # List of zeros with length of given value n
    seq = [0] * n
    seq[0] = seq[1] = 1

    # Algorithm Calculating Fibonacci Numbers
    for i in range(2,n):
        seq[i]= seq[i-1]+seq[i-2]
    
    return seq[n-1]

print(fibonacci(9))