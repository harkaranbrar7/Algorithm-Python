import time
import random

class Sorting:

    def __init__(self, arr):
        self.arr = arr

    def bubbleSort(self):
        n = len(self.arr)

        # Traverse through list 
        for i in range(n):
            for j in range(0,n-i-1):
                if self.arr[j] >self.arr[j+1]:
                    self.arr[j],self.arr[j+1]= self.arr[j+1],self.arr[j]
        
        return self.arr


    def insertionSort(self):
        for i in range(1,len(self.arr)):
            key = self.arr[i]

            j = i-1
            while j>=0 and key <self.arr[j]:
                self.arr[j+1]=self.arr[j]
                j-=1
            self.arr[j+1]=key
        
        return self.arr


    def selectionSort(self):

        # Trraverse through all elements of list 
        for i in range(len(self.arr)):
            min_idx = i
            for j in range(i+1,len(self.arr)):
                if self.arr[min_idx]>self.arr[j]:
                    min_idx = j
            
            # Swaping
            self.arr[i],self.arr[min_idx] = self.arr[min_idx],self.arr[i]
        
        return self.arr

    def output(self):
        print(self.arr)



#------------------------------------------------------------------------------
arr = [random.randint(1,10) for _ in range(10000)]
test1 = Sorting(arr)
print("-"*60)

start_time = time.time()
test1.bubbleSort()
end_time = time.time()
print("Total execution time Bubble Sort:    {}".format(end_time - start_time))


start_time = time.time()
test1.insertionSort()
end_time = time.time()
print("Total execution time Insertion Sort: {}".format(end_time - start_time))


start_time = time.time()
test1.selectionSort()
end_time = time.time()
print("Total execution time Selection Sort: {}".format(end_time - start_time))

print("-"*60)