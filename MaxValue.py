'''
Write a function solution that, given an integer N, 
returns the maximum possible value obtained by inserting one 
'5' digit inside the decimal representation of integer N. 

Examples: 
1. Given N 268, the function should return 5268. 
2. Given N 670, the function should return 6750. 
3. Given N 0, the function should return 50. 
4. Given N -999, the function should return -5999. 

Assume that: N is an integer within the range [-8,000.8,000]​

'''
def solution(N):
    # digit to add
    digit = '5' 
    # Create a List
    myList = []
    # convert absolute of int into String 
    temp = str(abs(N))

    # add digit to ech index
    for i in range(0,len(temp)+1):
        mystring = temp
        mystring = mystring[:i] + digit + mystring[i:] 
        myList.append(int(mystring))

    # if given int is negative 
    if N < 0:
        return -min(myList)
    
    return max(myList)


print("Highest Number will be:",solution(0))      #   50
print("Highest Number will be:",solution(268))    #   5268
print("Highest Number will be:",solution(670))    #   6750
print("Highest Number will be:",solution(-999))   #   -5999


