def bubbleSort(self,arr):
    n = len(arr)

    # Traverse through list 
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] >arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    
    return arr