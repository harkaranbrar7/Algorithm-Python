

class Solution:

    def __init__(self,str):
        self.str = str

    def sort(self):
        words = self.str.split()
        words.sort()
        return ' '.join((i) for i in words)


test1 = Solution(input("Enter a String: "))

print("The sorted words are:", test1.sort())

