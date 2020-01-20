def selectionSort(self,arr):

    # Trraverse through all elements of list 
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx = j
        
        # Swaping
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    
    return arr