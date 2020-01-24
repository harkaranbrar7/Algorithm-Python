'''
Write a function which accepts an integer array and its size and modifies the array in the following manner:

1) If the elements of index i and (i+1) are equal then, double the value at index i
and replace the element at index (i+1) with 0. 

2) If the element at index i is 0, then ignore it.

3) Any number (element in an array) must be modified only once.

4) At the end, shift all the zeros (0s) to the right of the array and remaining
nonzeros to the left of the array.

Example: 
Input: 2 2 0 4 0 8
Output: 4 4 8 0 0 0

Input: 2 2 0 4 0 2
Output: 4 4 2 0 0 0

'''

def solution(arr, n):

    for i in range(n-1): 
        if arr[i] == arr[i+1]:
            arr[i] = arr[i]*2
            arr[i+1] = 0

    return sorted(arr, key=lambda x: not x)  

    ''' OR '''

    # arr[:] = filter(None, arr)
    # arr.extend([0] * (n - len(arr)))
    # return arr


input1 = [2, 2, 0, 4, 0, 8]
length1 = len(input1)
print(solution(input1,length1))

input2  = [2, 2, 0, 4, 0, 2]
length2 = len(input2)
print(solution(input2,length2))



