
class Solution:

    def __init__(self, arr):
        self.arr = arr

    def bubbleSort(self):
        n = len(self.arr)

        for i in range(n):
            for j in range(0,n-i-1):
                if self.arr[j] >self.arr[j+1]:
                    self.arr[j],self.arr[j+1]= self.arr[j+1],self.arr[j]


    def insertionSort(self):
        for i in range(1,len(self.arr)):
            key = self.arr[i]

            j = i-j
            while j>=0 and key <self.arr[j]:
                self.arr[j+1]=self.arr[j]
                j-=1
            self.arr[j+1]=key