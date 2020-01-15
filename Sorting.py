
class Sorting:

    def bubbleSort(self,bSList):
        n = len(bSList)

        # Traverse through list 
        for i in range(n):
            for j in range(0,n-i-1):
                if bSList[j] >bSList[j+1]:
                    bSList[j],bSList[j+1]= bSList[j+1],bSList[j]
        
        return bSList


    def insertionSort(self,iSList):
        for i in range(1,len(iSList)):
            key = iSList[i]

            j = i-1
            while j>=0 and key <iSList[j]:
                iSList[j+1]=iSList[j]
                j-=1
            iSList[j+1]=key
        
        return iSList


    def selectionSort(self,sSList):

        # Trraverse through all elements of list 
        for i in range(len(sSList)):
            min_idx = i
            for j in range(i+1,len(sSList)):
                if sSList[min_idx]>sSList[j]:
                    min_idx = j
            
            # Swaping
            sSList[i],sSList[min_idx] = sSList[min_idx],sSList[i]
        
        return sSList

    def heapSort(self,arr):

        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            
            if l < n and arr[i] < arr[l]:
                largest = l 
            if r < n and arr[largest] < arr[r]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr [largest], arr[i]
                heapify(arr, n, largest)

            return arr

        def iheapSort(arr):
            n = len(arr)
            for i in range(n,-1,-1):
                heapify(arr, n , i)
            for i in range(n-1, 0 , -1):
                arr[i], arr[0] = arr[0],arr[i]
                heapify(arr, i, 0)
            
            return arr

        return iheapSort(arr)
 
    










