class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        n = x ^ y  
        setBits = 0
  
        while (n > 0) : 
            setBits += n & 1
            n >>= 1
      
        return setBits

test1 = Solution()
print(test1.hammingDistance(1,4))