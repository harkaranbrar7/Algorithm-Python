def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] >arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]


def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]

        j = i-j
        while j>=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key