
class Sort:
    
    def __init__(self, arr):
        self.arr = arr
        self.lengthOfArr = len(arr)

    def waveSort(self):

        for i in range(self.lengthOfArr):

            if i % 2 == 0: 
                
                if i>0 & self.arr[i-1]>self.arr[i]:
                    # Swap elements
                    self.arr[i], self.arr[i-1] = self.arr[i-1], self.arr[i]

                if i<=self.lengthOfArr-2:
                    if self.arr[i+1]>self.arr[i]:
                         # Swap elements
                        self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]

    def output(self):
        print(self.arr)
        


test1 = Sort([1,2,3,4,5,6,7])
test1.waveSort()
test1.output()

test1 = Sort([1,3,4,2,7,8])
test1.waveSort()
test1.output()

test1 = Sort([1,3,0,2,7,8])
test1.waveSort()
test1.output()