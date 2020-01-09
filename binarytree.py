def solution (arr):
    if not arr: return ""
    if len(arr) == 0: return ""; 

    def sum (arr, idx):
        if idx - 1 < len(arr): 
            if arr[idx - 1] == -1: return 0
            return arr[idx - 1] + sum(arr, idx * 2) + sum(arr, idx * 2 + 1)
        
        return 0

    left = sum(arr, 2)
    right = sum(arr, 3)
    
    if left == right:
        return ""
    if left > right:
        return "Left"
    else:
        return "Right"


print(solution([3,6,2,9,-1,10]))
#output Left
