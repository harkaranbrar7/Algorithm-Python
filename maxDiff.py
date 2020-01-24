'''
Write a function which accepts an integer array and its size and returns the maximum index difference i.e. (i-j) such that array[i] < array[j] and i < j. If there is no such case, return -1 .

Input: 2 0 3 5 6 1
Output: 6

There was only one test case given which is mentioned above. But I am providing the below
one of the sample cases which is an important thing to be noted. It returns -1 because all the
elements after any given element are smaller than it. DO take care of such cases.

Input: 9 8 7 6 5
Output: -1
'''

def maxDiff(arr, arr_size): 
    max_diff = arr[1] - arr[0] 
      
    for i in range( 0, arr_size ): 
        for j in range( i+1, arr_size ): 
            if(arr[j] - arr[i] > max_diff):  
                max_diff = arr[j] - arr[i] 
      
    return max_diff 
      
# Driver program to test above function  
arr = [2 ,0 ,3 ,5 ,6 ,1] 
size = len(arr) 
print ("Maximum difference is", maxDiff(arr, size)) 